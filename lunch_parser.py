# Grabs lunch menu and saves each day's menu to a file under menus/
# To be run once weekly (Sunday evening I suppose)

from lunch_menu_parser import Lunchbot
from lunch_menu_url_scraper import Menu

from datetime import date

menu = Menu()

url = menu.get_pdf_url()

bot = Lunchbot(url)

today = date.today().strftime('%A')

for day in bot.days_of_the_week:
    with open('menus/' + day + '.txt', 'w') as file:

        file.write(bot.get_day(day))

def read_menu(day):
    with open("menus/" + day + ".txt") as file:
        todays_menu = file.read()
        return todays_menu

