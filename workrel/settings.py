BOT_NAME = "workrel"

SPIDER_MODULES = ["workrel.spiders"]
NEWSPIDER_MODULE = "workrel.spiders"

ROBOTSTXT_OBEY = False
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"

DOWNLOAD_DELAY = 0.5
RANDOMIZE_DOWNLOAD_DELAY = True
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]
CONCURRENT_REQUESTS = 4
CONCURRENT_REQUESTS_PER_DOMAIN = 4

FEED_EXPORT_ENCODING = "utf-8"
LOG_LEVEL = "INFO"

FEEDS = {
    "data/landing/%(name)s_%(time)s.json": {
        "format": "json",
        "encoding": "utf-8",
        "indent": 2,
    }
}
