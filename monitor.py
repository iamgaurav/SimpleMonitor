import logging
import json
import requests
import os
from multiprocessing import Process

logging.basicConfig(level=logging.DEBUG, filename='monitor.log')

def slack(msg,exception):
    payload = {
        'username': os.getenv('slack_user'),
        "attachments": [ {
            "fallback": msg,
            "color": "#36a64f",
            "pretext":  msg,
            "text": exception,
        }],
    }
    request = requests.post(os.getenv('slack_web_hook'), json=payload)


def check_url(data, timeout):
    """
    Checks if the URL is up or not.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(data.get('url'), timeout=timeout, headers=headers)
        if response.status_code != data.get('status'):
            slack("Service Down: {0} Status Code: {1}".format(data.get('name'), response.status_code), str(response.headers))
        else:
            logging.info("Service: {} up".format(data.get('name')))
    except requests.exceptions.RequestException as e:
        logging.critical(e)
        slack("Service Down: {0}".format(data.get('name')), str(e))


procs = []


if __name__ == '__main__':

    """
    Loading the config.json
    """

    try:
        config = open('config.json')
        config = json.load(config)
        urls = config['services']
        os.environ['slack_web_hook'] = config['slack_web_hook']
        os.environ['slack_user'] = config['slack_user']
    except json.JSONDecodeError:
        logging.fatal("Invalid Json")
        exit(1)
    except KeyError as e:
        logging.fatal("Config Invalid. Missing {}".format(e.args))
        exit(1)
    except FileNotFoundError:
        logging.fatal("Config file not present. Please generate one using the config_generator.py")
        exit(1)

    if urls:
        for url in urls:
            process = Process(target=check_url, args=(url, config.get('timeout', 30,)))
            procs.append(process)
            process.start()
    for proc in procs:
        proc.join()
    exit(0)

