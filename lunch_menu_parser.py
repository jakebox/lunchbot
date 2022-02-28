###
###  FWP lunch menu parser
###  By Jake B
###  Original Sep 2019, improved Oct 2019, improved & class-ified Nov 2021
###

import pdftotext
from six.moves.urllib.request import urlopen
import io
import sys


class Lunchbot:
    def __init__(self, url):
        # Getting the lunch menu PDF and putting it into a variable
        remote_file = urlopen(url).read()
        memory_file = io.BytesIO(remote_file)
        pdf = pdftotext.PDF(memory_file)
        self.pdf_content = pdf[0]

        # Creating dictionary to hold the location of each day's meal list in the list
        self.dict = {"Monday:": 0, "Tuesday:": 0, "Wednesday:": 0, "Thursday:": 0, "Friday:": 0}
        self.days_of_the_week = ["Mon", "Tues", "Wednes", "Thurs", "Fri"]

        self.parse_pdf()


    def parse_pdf(self):
        # Turning the string into list (each word is its own element)
        self.menu = self.pdf_content.split()
        
        # Removing weird unicode chars (bullet points)
        for index, item in enumerate(self.menu):
            if item == "\uf0b7": self.menu.remove(item)
            if item == "•": self.menu[index] = "\n •"
            # These two lines make sure that minor typos in the day make it thru
            for day in self.days_of_the_week:
                if day in item: self.menu[index] = day + "day:"

        # self.menu[self.menu.index('Tuesday:3/1')] = "Tuesday:" # Stupid fix for a typo

        # Finding and setting the location of each day's meal list beginning
        for day, spot in self.dict.items():
            self.dict[day] = self.menu.index(day)


    def get_day(self, day):
        # Finding and setting the end of each day's meal list. Could probably be shorter.
        if day == "M":
            day = "Monday"
            end_day_pos = self.menu.index("Tuesday:")
        elif day == "T":
            day = "Tuesday"
            end_day_pos = self.menu.index("Wednesday:")
        elif day == "W":
            day = "Wednesday"
            end_day_pos = self.menu.index("Thursday:")
        elif day == "Th":
            day = "Thursday"
            end_day_pos = self.menu.index("Friday:")
        elif day == "F":
            day = "Friday"
            end_day_pos = len(self.menu)

        return ' '.join(self.menu[self.dict.get(day + ":"):end_day_pos])


if __name__ == '__main__':

    # This method is outdated, use lunch_parser cached menus

    day_requested = "T"
    url = 'https://fwparker.myschoolapp.com/ftpimages/1048/download/download_6209679.pdf'

    bot = Lunchbot(url)

    todays_menu = bot.get_day(day_requested)

    print(todays_menu)
