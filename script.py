from telethon import TelegramClient, events
import requests
import json
import os
 
# my.telegram.org
api_id =   
api_hash = ''
phone = ''
client = TelegramClient(phone, api_id, api_hash)

async def main():

    ip = get_ip()
    temp = get_temperature()
    uptime = get_uptime()
    message = await client.send_message(
        # recipient
        '',
        '**::LOG::**' + '\n' +
        ' **IP:: **' + ip + '\n' +
        ' **Temperature:: **' + temp + 
        ' **Uptime:: **' + uptime ,
        link_preview=False
    )


def get_ip():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)
    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()
    data = response.json()
    return data['ip']

def get_temperature():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")

def get_uptime():
    uptime = os.popen("uptime").readline(35)
    return uptime


with client:
    client.loop.run_until_complete(main())