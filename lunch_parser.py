# Grabs lunch menu and saves it to a file. Combines other two .py files.
# To be run once weekly (Sunday evening I suppose).

from lunch_menu_parser import Lunchbot
from lunch_menu_url_scraper import Menu

from datetime import date
import os
import requests

days_of_the_week = ["M", "T", "W", "Th", "F"]
local_menu_file = "menu.txt"

def get_menus():
    "Take menu from Internet and save as plaintext file menu.txt."

    menu = Menu() # lunch_menu_url_scraper.py

    url = menu.get_pdf_url() # Scrape and return URL of lunch menu

    bot = Lunchbot(url) # lunch_menu_parser.py, parse PDF from given URL


    with open(local_menu_file, 'w') as file: # Write each day's menu to file
        for day in days_of_the_week:
            file.write(bot.get_day(day) + '\n\n')


remote_menu_url = "https://fwp-lunchbot.s3.us-east-2.amazonaws.com/menus/menu.txt"

def read_parsed_text_menu(remote=False): # Get contents of menu file
    "Read contents of menu file."
    if remote:
        remote_menu = requests.get(remote_menu_url)
        remote_menu.encoding = remote_menu.apparent_encoding
        return(remote_menu.text.strip())
    else:
        with open(local_menu_file) as file:
            menu = file.read()
            return menu.strip() # Return full menu text with no extra whitespace at bottom


if __name__ == '__main__':
    # print("Scraping, parsing, and saving menu.")
    # get_menus()
    print("Reading from remote url", remote_menu_url + "\n")
    print(read_parsed_text_menu(True))
