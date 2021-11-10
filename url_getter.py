import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class Menu:
    def __init__(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        ua=UserAgent()
        hdr = {'User-Agent': ua.random,
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

        url = 'https://www.fwparker.org/weekly-lunch-order-form'
        req = requests.get(url, headers=hdr)
        soup = BeautifulSoup(req.content, 'html.parser')
        self.div_i_want = soup.find_all("div", {"id": "content_2494555"})

    def get_pdf_url(self):
        "Extract menu URL."
        for div in self.div_i_want:
            if div.find('a')['href']:
                lunch_menu_url = div.find('a')['href']
        return lunch_menu_url
        

if __name__ == '__main__':
    menu = Menu()

    menu_pdf_url = menu.get_pdf_url()

    print(menu_pdf_url)
