# Model-Level Validators

from datetime import date
from pydantic import BaseModel, ValidationError


# how to check if start date
class ScheduledCourse(BaseModel):
    department: str
    course_number: int
    start_date: date
    end_date: date

#Validate days

from pydantic import model_validator

class ScheduledCourse(BaseModel):
    department: str
    course_number: int
    start_date: date
    end_date: date

    @model_validator(mode = "before") #called before all other things in class
    @classmethod
    def validate_dates(cls, data: dict):
        if data["start_date"] > data["end_date"]:
            raise ValueError("Start date must be before end date")
        return data

try:
    course = ScheduledCourse(start_date="2024-12-22",
                             end_date="2024-11-10")  #Value error, Start date must be before end date
    print(course)
except ValidationError as e:
    print(e)



#After mode

class ScheduledCourse(BaseModel):
    department: str
    course_number: int
    start_date: date
    end_date: date

    @model_validator(mode = "after") #called the last one in the class
    def validate_dates(self):
        #if data["start_date"] > data["end_date"]:
            #raise ValueError("Start date must be before end date")
        #return data

        if self.start_date > self.end_date:
            raise ValueError("Start date must be after end date")
        return self
try:
    course = ScheduledCourse(start_date="2024-12-22",
                             end_date="2024-11-10")
    print(course)
except ValidationError as e:
    print(e)

    #Now we have an error with missed field. But before we had about not appropriate data