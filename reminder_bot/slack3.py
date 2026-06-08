from dotenv import load_dotenv
from course_dates3 import due_dates

import os
from slack_sdk import WebClient

load_dotenv("creds.env")

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
client = WebClient(token=SLACK_TOKEN)


from datetime import datetime, timezone
today = datetime.now(timezone.utc)

message = ""
for d in due_dates:
    days_left = (d.date.date() - today.date()).days

    print(f"{d.title}: {days_left}")

    if days_left == 1:

        if message == "":
            message = "📅 Upcoming Deadline\n\n\n"
            message += "📘 Course: Python Capstone\n\n"

        message += f" 📌 Module: {d.title}\n"
        
        timestamp = int(d.date.timestamp())
        message += f"🗓️ Deadline (Local Time): <!date^{timestamp}^{{date_short}} {{time}}|{d.format_date()}>\n" 
        message += f"🌍 Deadline (UTC): {d.format_date()}\n"
        message += f"⏳ Days remaining: {days_left}\n\n"   

if message != "":
    client.chat_postMessage(
        channel="#python_capstone-deadline-reminders",
        text=message
)

print("Upcoming Deadlines test message sent successfully")
print(message)