# Goal:
# Step 1: Crawl all the URL
# Step 2: Pass data to scrapper and scrape all price + data based on query
# Step 3: Preprocess data
# Step 4: Add to database

from bs4 import BeautifulSoup
import requests


def get_page_from_url(url: str = ""):
    if url == "":
        raise Exception("No URL provided")
    try:
        page = requests.get(url)
        return page.content
    except:
        raise Exception("Stuff gone wrong")


def is_valid_url(url: str = ""):
    if url == "" or url == None:
        return False
        
    # Other validations
    
    cleaned_url = url.strip() or url
    print(cleaned_url)
    return ("http://" in cleaned_url) or ("https://" in cleaned_url)



class Crawler:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup
        self.urls = []

    def collect_urls(self):
        try:
            if self.soup:
                for link in self.soup.find_all('a', href=True):
                    is_valid = is_valid_url(link['href'])
                    if is_valid:
                        self.urls.append(link['href'])
                print(self.urls)
        except:
            raise Exception("Stuff gone wrong")


class MasterCrawler:
    def __init__(self, seed) -> None:
        self.seed = seed
        self.crawlers = []
        pass

    def spawn_crawler(self) -> None:
        page = get_page_from_url(self.seed)
        soup = BeautifulSoup(page, 'html.parser')
        cralwer = Crawler(soup=soup)
        
        self.crawlers.append(cralwer)
        cralwer.collect_urls()


def test():
    url = "https://crawler-test.com/links/max_external_links"
    if is_valid_url(url):
        master_crawler = MasterCrawler(url)
        master_crawler.spawn_crawler()


test()
