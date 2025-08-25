## de-workrel-scraper

### Requirements
- Python 3.10+
- pip

### Setup
```
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

### Run the spider
Default run (outputs JSON to `data/landing/` via FEEDS):
```
scrapy crawl workrel
```

Run with a date range (DD/MM/YYYY):
```
scrapy crawl workrel -a from_date=01/07/2025 -a to_date=21/08/2025
```

### Output
- Files are written to `data/landing/%(name)s_%(time)s.json` (pretty-printed UTF-8).

