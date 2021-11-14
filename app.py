from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import Message, MessagingResponse

import sys
from datetime import date

# from lunch_parser import read_parsed_text_menu

days_of_the_week = ["M", "T", "W", "Th", "F"]

app = Flask(__name__)

today = date.today().strftime('%A')

remote_menu_url = "https://fwp-lunchbot.s3.us-east-2.amazonaws.com/menus/menu.txt"

def read_parsed_text_menu(): # Get contents of menu file
    "Read contents of menu file."
    remote_menu = requests.get(remote_menu_url)
    remote_menu.encoding = remote_menu.apparent_encoding
    return(remote_menu.text.strip())

@app.route('/sms', methods=['POST'])
def sms():

    number = request.form['From']
    message_body = request.form['Body'].title().strip()
    resp = MessagingResponse()

    resp.message(read_parsed_text_menu(True))

    return str(resp)

if __name__ == '__main__':
    app.run()
    # message_body = sys.argv[1]

    # if message_body in days_of_the_week: # If the message is something we know how to do
    #     todays_menu = read_menu(message_body)
    # elif today[0] in days_of_the_week or today[0:1] in days_of_the_week: # Tuesday and Thursday
    #     if today == "Thursday":
    #         todays_menu = read_menu("Th")
    #     else:
    #         todays_menu = read_menu(today[0])
    # else:
    #     todays_menu = read_menu("M")
    # print(todays_menu + '\n \nSponsored by CTC/Student Government & FTC Robotics')
    
