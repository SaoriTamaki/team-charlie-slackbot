import json

from reminder_bot.openedx import get_deadlines, get_dates

deadlines = get_deadlines()
print("DEADLINES:")
print(deadlines)

dates = get_dates()
print("DATES:")
print(json.dumps(dates, indent=2))



