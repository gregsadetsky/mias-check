import re
from pathlib import Path

PARENT_DIR = Path(__file__).resolve().parent
MIASDB_TRUTH_FILE = PARENT_DIR / "0.miasdb.txt"
PREDICTIONS_FILE = PARENT_DIR / "3.output.csv"

known_malignant_ids = []
with open(MIASDB_TRUTH_FILE) as f:
  for line in f:
    parts = line.strip().split()
    if 'M' in parts:
      known_malignant_ids.append(parts[0].removeprefix('mdb'))

true_pos = 0
true_neg = 0
false_pos = 0
false_neg = 0

with open(PREDICTIONS_FILE) as f:
  for line in f:
    file_name, prediction = line.strip().split(',')
    file_id = re.match(r'^mdb(\d+)\D+.jpg$', file_name).groups()[0]
    prediction = (prediction == 'True')

    if prediction is False and file_id not in known_malignant_ids:
      true_neg += 1
    elif prediction is False and file_id in known_malignant_ids:
      false_neg += 1
    elif prediction is True and file_id not in known_malignant_ids:
      false_pos += 1
    elif prediction is True and file_id in known_malignant_ids:
      true_pos += 1

print('true_pos', true_pos)
print('true_neg', true_neg)
print('false_pos', false_pos)
print('false_neg', false_neg)
print('total', true_pos + true_neg + false_pos + false_neg)
