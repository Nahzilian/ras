from modules.crawl import MasterCrawler, is_valid_url
from modules.scrape import Scraper

def main():
    url = "https://stackoverflow.com/questions/31958637/beautifulsoup-search-by-text-inside-a-tag"
    if is_valid_url(url):
        master_crawler = MasterCrawler(url)
        master_crawler.spawn_crawler()
        soup = master_crawler.get_soup()
        scraper = Scraper(soup)
        scraper.scrape_items()
        print(scraper)

main()