# Field Exclusions

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

#print(course.model_dump_json())  # -> {"department":"CS","course_number":101,"start_date":"2024-01-23","end_date":"2024-01-24"}

print(course.model_dump_json(exclude={"department", "course_number"})) # -> {"start_date":"2024-01-23","end_date":"2024-01-24"}
print(course.model_dump_json(include={"department", "course_number"}))  # -> {"department":"CS","course_number":101}

#excldude_unset


class ScheduledCourse(BaseModel):
    department: str = "?"
    course_number: int
    start_date: date = date.today()
    end_date: date


    @model_validator(mode="after")
    def validate_dates(self):
        if self.start_date > self.end_date:
            raise ValueError("Start date must be after end date")
        return self

course = ScheduledCourse(
    course_number=101,
    end_date="2026-01-24"
)
print(course.model_dump_json(exclude_unset=True)) #We are not use the data that not requirement in our basemodel


course = ScheduledCourse(
    course_number=101,
    end_date="2026-01-24",
    department="?"
)
print(course.model_dump_json(exclude_unset=True)) # -> {"department":"?","course_number":101,"end_date":"2026-01-24"}
print(course.model_dump_json(exclude_defaults=True)) # -> {"course_number":101,"end_date":"2026-01-24"}

