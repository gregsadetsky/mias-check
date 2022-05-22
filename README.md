# what is this

an extremely informal test of the mammogram analysis tool described [here](https://news.ycombinator.com/item?id=31449147)

## results

```
true_pos 36
true_neg 207
false_pos 63
false_neg 16
total 322
```

## see analyzed / scraped data

- html results returned for all images are under the `_scraping` directory
- the tool's "analyzed" results are in `3.output.csv` (true/false value meaning "is the word malignant present on the result page")

## how to run it / reproduce it

- download the source images

```
cd 0.data
./download.sh
```

- pip install beautifulsoup and requests if missing
- run:

```
# this takes a while since it submits every image
python3 1.analyze.py
python3 4.validate_results.py
```

## next/todo

- compare position of masses (truth vs prediction)
- take return prediction 'possibility' into account

## credits

- Suckling, J., Parker, J., Dance, D., Astley, S., Hutt, I., Boggis, C., Ricketts, I., et al. (2015). Mammographic Image Analysis Society (MIAS) database v1.21 \[Dataset\]. https://www.repository.cam.ac.uk/handle/1810/250394
