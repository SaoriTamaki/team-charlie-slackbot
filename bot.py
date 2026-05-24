import os
from slack_sdk import WebClient


SLACK_TOKEN = os.environ["SLACK_TOKEN"]

client = WebClient(token=SLACK_TOKEN)
client.chat_postMessage(channel='#all-team-charlie-workspace',text='Test successful: Python was able to send a message to the Slack app channel')