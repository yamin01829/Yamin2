import urllib.request
from bs4 import BeautifulSoup
import ssl
import time
import os
import sys

ssl._create_default_https_context = ssl._create_unverified_context

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Android 10; Mobile)"
}

CATEGORIES = {
    "Bangla_Movie": "https://www.notunmovie.link/category/bangla-movie/",
    "Bangla_Natok": "https://www.notunmovie.link/category/bangla-natok/",
    "Bangla_Web_Series": "https://www.notunmovie.link/category/bangla-web-series/",
    "Kolkata_Movie": "https://www.notunmovie.link/tag/kolkata-movie/",
    "Bangla_Dubbing_Movie": "https://www.notunmovie.link/category/bangla-dubbing-movie/",
    "Bangla_Dubbing_Web_Series": "https://www.notunmovie.link/category/bangla-dubbing-web-series/",
    "Hindi_Movie": "https://www.notunmovie.link/category/hindi-movie/",
    "Hindi_Dubbed_Movie": "https://www.notunmovie.link/category/hindi-dubbed-movie/",
    "Hindi_Web_Series": "https://www.notunmovie.link/category/hindi-web-series/",
    "Bangla_Hot_Web_Series": "https://www.notunmovie.link/category/bangla-hot-web-series-collection/"
}

def scrape():
    if not os.path.exists("shuvo"):
        os.makedirs("shuvo")

    for name, url in CATEGORIES.items():
        print(f"Scraping {name}")
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            html = urllib.request.urlopen(req, timeout=30).read()
            soup = BeautifulSoup(html, "html.parser")

            links = set()
            for a in soup.find_all("a", href=True):
                link = a["href"]
                if "notunmovie.link" in link:
                    links.add(link)

            with open(f"shuvo/{name}.txt", "w", encoding="utf-8") as f:
                for l in sorted(links):
                    f.write(l + "\n")

            time.sleep(2)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    scrape()
