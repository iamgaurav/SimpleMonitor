import logging
import json
import requests
from multiprocessing import Process

"""
Loading the config.json
"""

try:
    config = open('config.json')
    config = json.load(config)
    urls = config['services']
except json.JSONDecodeError:
    logging.fatal("Invalid Json")
    exit(1)
except KeyError as e:
    logging.fatal("Config Invalid. Missing {}".format(e.args))
    exit(1)
except FileNotFoundError:
    logging.fatal("Config file not present. Please generate one using the config_generator.py")
    exit(1)


def check_url(data, timeout):
    """
    Checks if the URL is up or not.
    """
    try:
        response = requests.get(data.get('url'), timeout=timeout).elapsed.total_seconds()
        print(response)
    except requests.exceptions.RequestException as e:
        logging.critical(e)


procs = []


if __name__ == '__main__':
    if urls:
        for url in urls:
            process = Process(target=check_url, args=(url, config.get('timeout', 30,)))
            procs.append(process)
            process.start()
    for proc in procs:
        proc.join()
    exit(0)