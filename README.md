# Simple Monitor Service

This is a simple URL monitoring script which can also notify a channel on slack
if a particular service is down.

## Setup

The script uses the requests package which can be installed using the requirements.txt

`pip3 install requirements.txt`

## Config

The script comes with a config generator which can be used to create/update an existing configuration file.

By running the following file:

`python3 config_generator.py`

## Run

The script can be added to the crontab based on the interval period you want to check the URL status for.

Example
```
*/15 * * * * /usr/bin/python3 monitor.py # runs every 15 minutes.
```