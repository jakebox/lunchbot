from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import Message, MessagingResponse

from lunch_bot_getter import Lunchbot
from url_getter import Menu

from datetime import date

app = Flask(__name__)

menu = Menu()

url = menu.get_pdf_url()

bot = Lunchbot(url)

# url = 'https://fwparker.myschoolapp.com/ftpimages/1048/download/download_6209679.pdf'


today = date.today().strftime('%A')

@app.route('/sms', methods=['POST'])
def sms():

    number = request.form['From']
    message_body = request.form['Body'].title().strip()
    resp = MessagingResponse()

    if message_body in bot.days_of_the_week: # If the message is something we know how to do
        todays_menu = bot.get_day(message_body)
    elif today[0] in bot.days_of_the_week or today[0:1] in bot.days_of_the_week:
        if today == "Thursday":
            todays_menu = bot.get_day("Th")
        else:
            todays_menu = bot.get_day(today[0])
    else:
        todays_menu = bot.get_day("M")
    resp.message(todays_menu + '\n \nSponsored by CTC/Student Government & FTC Robotics')

    return str(resp)

if __name__ == '__main__':
    app.run()
