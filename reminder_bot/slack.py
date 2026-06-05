from dotenv import load_dotenv
from course_dates import due_dates

import os
from slack_sdk import WebClient

load_dotenv("creds.env")

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
client = WebClient(token=SLACK_TOKEN)


from datetime import datetime
today = datetime.now()

message = ""
for d in due_dates:
    days_left = (d.date.date() - today.date()).days
    if days_left == 3:

        if message == "":
            message = "📅 Upcoming Deadline\n\n\n"
            message += "📘 Course: Python Capstone\n\n"

        message += f" 📌 Module: {d.title}\n"
        message += f" 🗓️ Due: {d.format_date()}\n\n"    


client.chat_postMessage(
    channel="#python_capstone-deadline-reminders",
    text=message
)

print("pcoming Deadlines test message sent successfully")
print(message)