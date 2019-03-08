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