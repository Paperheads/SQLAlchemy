#Lection Date_time

from datetime import date

# 2024-01-01
import pydantic
from pydantic import BaseModel

class Event(BaseModel):
    event_date: date

try:
    event = Event(event_date = '2024-03-03')
    print(event)
except pydantic.ValidationError as e:
    print(e)



#additional specify time component
from datetime import time

class Event(BaseModel):
    event_date: date
    event_time: time

try:
    event = Event(event_date = '2024-03-03', event_time="14:30:00")
    print(event)
except pydantic.ValidationError as e:
    print(e)


#Best option
from datetime import datetime

class Appointment(BaseModel):

    start_time : datetime


try:
    appt = Appointment(start_time = datetime.now())
    print(appt) # start_time=datetime.datetime(2025, 3, 19, 16, 54, 4, 503897)
except pydantic.ValidationError as e:
    print(e)

print(appt.start_time) #2025-03-19 16:54:31.721187