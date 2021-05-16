import requests

from main import getToken, url

BOT_TOKEN = getToken()


def isNotifications():
    r = requests.get(f"{url}/notifications")
    if r.status_code == 200:
        return True
    else:
        return False


def receiveNotifications():
    r = requests.get(f"{url}/notifications")
    return r.json()


def sendNotifications():
    receivedata = receiveNotifications()
    headers = {
        'Content-type': 'application/json',
    }
    for notification in receivedata['data']:

        chat_id = notification['tg_id']
        text = notification['message']

        data = '{"text":"' + text + '", "chat_id":"' + str(chat_id) + '"}'
        curl = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage'

        response = requests.post(curl, headers=headers, data=data)
    return response


if __name__ == '__main__':
    if isNotifications():
        send = sendNotifications()


