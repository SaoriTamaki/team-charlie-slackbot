from openedx3 import get_dates
from datetime import datetime, timezone


#define class for extracting due dates:
class CourseDate:
    def __init__(self, date_type: object, title: object, date: object):
        self.date_type = date_type
        self.title = title
        self.date = date


    def format_date(self):
        return self.date.strftime("%d.%m.%Y %H:%M")

    def format_date_type(self):
        #get date_type
        raw_date_type = self.date_type

        # remove -
        cleaned_date_type = raw_date_type.replace("-", " ").title()

        return cleaned_date_type


    def __str__(self):
        return f"{self.title}: {self.format_date()}"


#method for extracting due dates
def extract_dates(data, date_type):
    dates = []
    now = datetime.now(timezone.utc)

    for d in data["course_date_blocks"]:
        # get date
        raw_date = d["date"]

        #check if due date is set
        if raw_date is not None:

            #change Json string to date format
            # remove Z
            cleaned_date = raw_date.replace("Z", "+00:00")
            # transform cleaned_date to date formate
            dt = datetime.fromisoformat(cleaned_date)

            #check if due date is in the future
            if dt>=now:

                #create object of class CourseDate
                due_information=CourseDate(
                    d["date_type"],
                    d["title"],
                    dt)
                #safe in dates list
                dates.append(due_information)
    return dates




#get extracted data
data = get_dates()
due_dates = extract_dates(data, None)

message = "📅 Upcoming Deadlines:\n\n"

for d in due_dates:
    message += f"• {d}\n"

#print extracted data
print(message)
