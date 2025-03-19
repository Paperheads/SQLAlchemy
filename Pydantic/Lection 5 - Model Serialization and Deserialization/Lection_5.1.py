# Model Serialization and Deserialization
# Instance Serialization to DICT and JSON


'''
Serialization -> is a process of converting data from one format to another.
The most popular is JSON and DICT
'''

from datetime import date
from pydantic import BaseModel, model_validator


class ScheduledCourse(BaseModel):
    department: str
    course_number: int
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def validate_dates(self):
        if self.start_date > self.end_date:
            raise ValueError("Start date must be after end date")
        return self


course = ScheduledCourse(
    department="CS",
    course_number=101,
    start_date="2024-01-23",
    end_date="2024-01-24"
)

print(course.model_dump()) # -> {'department': 'CS', 'course_number': 101, 'start_date': datetime.date(2024, 1, 23), 'end_date': datetime.date(2024, 1, 24)}
print(course.model_dump_json()) # -> {"department":"CS","course_number":101,"start_date":"2024-01-23","end_date":"2024-01-24"}