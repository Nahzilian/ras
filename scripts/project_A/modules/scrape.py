from bs4 import BeautifulSoup
from .files import write_to_file
# Look at site, select template and scrape specific items
# Future note: Let AI handle it?


class Scraper:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup
        self.text = []
    
    def scrape_items(self):
        # Extracting data from body
        parent = self.soup.body
        text_list = []
        
        # ++++++ Original method +++++++
        # N -ary tree search
        # Searching for each node, if node has content => Extract and assign depth
        # IDC about hierarchy
        # def search_tree(parent: BeautifulSoup, depth: int):
        #     if len(parent.children) > 0:
        #         if parent.contents:
        # ++++++++++++++++++++++++++++++
        
        for child in parent.descendants:
            if child and child.text and child.text != "":
                text_list.append(child.text)
                
        self.text = text_list
        write_to_file("temp", '\n'.join(self.text))
        
    def __str__(self) -> str:
        text = '\n'.join(self.text)
        return text