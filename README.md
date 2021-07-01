# Population Scraper
## Table of contents
- [Description](#description)
- [Extracted Data](#extracted-data)
- [Spiders](#spiders)
- [How to setup](#how-to-use)

## Description
This is a scrapy project, which scrapes population of countries from https://www.worldometers.info/ 
## Extracted Data
This project extracts country, year and respective population. The extracted data looks like this sample:
```
{
    "country_name": "India",
    "year": "1955",
    "population": "409,880,595"
}

```
## Spiders
This project has the spider `countries.py`.

## How to use
You can run a spider using the scrapy crawl command, such as:
```
scrapy crawl countries
```
To save the extracted data, use `-o` option followed by filename with above command:
```
scrapy crawl countries -o population_dataset.json
```
