# what is this

an extremely informal test of the tool described [here](https://news.ycombinator.com/item?id=31449147)

## results

```
true_pos 36
true_neg 207
false_pos 63
false_neg 16
total 322
```

## see analyzed / scraped data

- the tool's html results are under the `_scraping` directory
- the tool's "analyzed" results are in `3.output.csv`
-- it boils down to "is the word malignant present on the output page"

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
