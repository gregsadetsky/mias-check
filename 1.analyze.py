import os
import requests
from pathlib import Path
from bs4 import BeautifulSoup


ENDPOINT = 'http://mammo.neuralrad.com:5300/upload'
PARENT_DIR = Path(__file__).resolve().parent
DATA_DIR = PARENT_DIR / "0.data/MIASDBv1.21"
SCRAPING_DIR = PARENT_DIR / "2.scraping"
OUT_FILE = PARENT_DIR / "3.output.csv"

if not os.path.isdir(DATA_DIR):
  raise Exception('please download & unzip the MIASDBv1.21 directory under 0.data')

file_names = filter(lambda _: _.endswith('.jpg'), os.listdir(DATA_DIR))

all_predictions = []

for file_name in file_names:
  r = requests.post(ENDPOINT, data={
    'submit': 'Analyze'
  }, files=[
    ('file', open(DATA_DIR / file_name, 'rb'))
  ], headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
  })

  with open(SCRAPING_DIR / "{}.html".format(file_name), 'wb') as f:
    f.write(r.content)

  soup = BeautifulSoup(r.content, 'html.parser')
  page_predictions = ' '.join(map(
    lambda p: p.text,
    soup.find_all('section')[1].findAllNext('p')[1:]
  )).lower()
  predicted_malignant = 'malignant' in page_predictions

  all_predictions.append(','.join([file_name, str(predicted_malignant)]))

with open(OUT_FILE, 'w') as f:
  for prediction in all_predictions:
    f.write('{}\n'.format(prediction))
