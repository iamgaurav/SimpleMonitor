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

This will generate a config.json file with the following structure

```
{
   "timeout": 30,
   "slack_user": "Slack Username",
   "slack_web_hook":"Slack Webhook URL",
   "services":[
      {
         "name":"Domain Name",
         "url":"URL",
         "status":200 # Matches the status code
      }
   ]
}
```

## Run

The script can be added to the crontab based on the interval period you want to check the URL status for.

Example
```
*/15 * * * * /usr/bin/python3 monitor.py # runs every 15 minutes.
```