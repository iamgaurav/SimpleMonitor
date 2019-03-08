import os
import json

if __name__ == "__main__":
    print("This script generates the config.json required for the monitor.py script")
    try:
        config = open('config.json', 'r')
        config = json.load(config)
        print("Found an existing config.json. This script will add new data to the existing json")
    except:
        config = {}
        print("Creating a new config.json")

    if "services" in config:
        print("To add a new service please provide the name and url")
        name, url = input("name:"), input("url:")
        config['services'].append({'name': name, 'url': url})
    else:
        timeout = input("timeout:")
        print("To add a new service please provide the name and url")
        name, url = input("name:"), input("url:")
        config['timeout'] = int(timeout)
        config['services'] = []
        config['services'].append({'name': name, 'url': url})

    """
    Updating the config.json with the data
    """
    final_config = open('config.json', 'w+')
    final_config.writelines(json.dumps(config))
