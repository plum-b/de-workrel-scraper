import urllib.parse as up
from datetime import datetime
import scrapy

class WorkPlaceRelationsSpider(scrapy.Spider):
    name = "workrel"
    allowed_domains = ["workplacerelations.ie"]

    def __init__(self, from_date="1/1/2025", to_date="31/12/2025", pageNumber="1", **kwargs):
        super().__init__(**kwargs)
        self.base = "https://www.workplacerelations.ie/en/search/"
        self.q = {"decisions": "1", "from": from_date, "to": to_date, "pageNumber": str(pageNumber)}
        self.start_urls = [f"{self.base}?{up.urlencode(self.q)}"]

        self._fallback_partition = None
        try:
            fd = datetime.strptime(from_date, "%d/%m/%Y")
            self._fallback_partition = fd.strftime("%Y-%m")
        except Exception:
            pass

    def parse(self, response):
        for li in response.css("li.each-item"):
            identifier = li.css("h2.title a::text").get(default="").strip() or None
            date_str = li.css(".date::text").get(default="").strip() or None
            desc = li.css("p.description::text").get(default="").strip() or None
            href = li.css("h2.title a::attr(href)").get()
            url = response.urljoin(href) if href else None

            code = None
            if identifier:
                code = identifier.replace(" - ", "-").replace(" ", "")

            partition_date = self._fallback_partition
            if date_str:
                try:
                    dt = datetime.strptime(date_str, "%d/%m/%Y")
                    partition_date = dt.strftime("%Y-%m")
                except Exception:
                    pass

            yield {
                "identifier": identifier,
                "code": code,
                "date": date_str,
                "description": desc,
                "link_to_doc": url,
                "source_page": response.url,
                "partition_date": partition_date
            }

        items_found = bool(response.css("li.each-item"))
        if items_found:
            parsed = up.urlparse(response.url)
            qs = dict(up.parse_qsl(parsed.query))
            try:
                nxt = int(qs.get("pageNumber", "1")) + 1
                qs["pageNumber"] = str(nxt)
                next_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{up.urlencode(qs)}"
                yield scrapy.Request(next_url, callback=self.parse)
            except ValueError:
                return
