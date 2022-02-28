from flask import Flask, request

import sys
import requests
from datetime import date

import os

telnyx_api_key = "KEY017D6900D5CE1F9E3A37F3C50637B764_327Pr2tHI9UFyVlY7Kfv9X"
telnyx_number = "+12182203065"

days_of_the_week = ["M", "T", "W", "Th", "F"]

app = Flask(__name__)

today = date.today().strftime('%A')

remote_menu_url = "https://fwp-lunchbot.s3.us-east-2.amazonaws.com/menus/menu.txt"

def send_message(number, message):
    # message="Lunch menu here:"
    command = "curl -X POST \\\n  --header \"Content-Type: application/json\" \\\n  --header \"Authorization: Bearer " + telnyx_api_key + "\" \\\n  --data \'{\n    \"from\": \"" + telnyx_number + "\",\n    \"to\": \"" + number + "\",\n    \"text\": \"" + message + "\"\n  }\' \\\n  https://api.telnyx.com/v2/messages\n"
    os.system(command)
    

def read_parsed_text_menu(): # Get contents of menu file
    "Read contents of menu file."
    remote_menu = requests.get(remote_menu_url)
    remote_menu.encoding = remote_menu.apparent_encoding
    return(remote_menu.text.strip().replace("\n", "\\n"))

@app.route('/webhooks', methods=['POST'])
def webhooks():
    body = request.json
    texter_number = body['data']['payload']['from']['phone_number']

    if texter_number != "+12182203065":
        print(texter_number)
        print("Text recieved from: ", texter_number)

        send_message(texter_number, read_parsed_text_menu().replace("\n", "\\n"))

    return '', 200

if __name__ == '__main__':
    app.run(port=8000)
    # print(repr(read_parsed_text_menu().replace("\n", "\\n")))
    # print(read_parsed_text_menu())
