# JSON Schema
"""
• what are schemas?

•schemas are blueprints for data structures
•they describe the shape of a structure in the abstract
•widely useful in codegen, documentation, automation, etc.
•JSON Schema is the dominant standard in the JSON ecosystem
"""

from datetime import date
from pydantic import BaseModel, model_validator
from pydantic.json_schema import model_json_schema


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


print(ScheduledCourse.model_json_schema())
#{'properties': {'department': {'title': 'Department', 'type': 'string'}, 'course_number': {'title': 'Course Number', 'type': 'integer'},
# 'start_date': {'format': 'date', 'title': 'Start Date', 'type': 'string'}, 'end_date':
# {'format': 'date', 'title': 'End Date', 'type': 'string'}}, 'required': ['department', 'course_number', 'start_date', 'end_date'],
# 'title': 'ScheduledCourse', 'type': 'object'}

import json

print(json.dumps(ScheduledCourse.model_json_schema(), indent = 2))
"""
{
  "properties": {
    "department": {
      "title": "Department",
      "type": "string"
    },
    "course_number": {
      "title": "Course Number",
      "type": "integer"
    },
    "start_date": {
      "format": "date",
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "format": "date",
      "title": "End Date",
      "type": "string"
    }
  },
  "required": [
    "department",
    "course_number",
    "start_date",
    "end_date"
  ],
  "title": "ScheduledCourse",
  "type": "object"
}
"""

#Second model
from typing import List, Optional

class Item(BaseModel):
    name : str
    description : Optional[str] = None

class Order(BaseModel):
    id : int
    items : List[Item]

print(json.dumps(Order.model_json_schema(), indent = 2))

"""
{
  "$defs": {
    "Item": {
      "properties": {
        "name": {
          "title": "Name",
          "type": "string"
        },
        "description": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Description"
        }
      },
      "required": [
        "name"
      ],
      "title": "Item",
      "type": "object"
    }
  },
  "properties": {
    "id": {
      "title": "Id",
      "type": "integer"
    },
    "items": {
      "items": {
        "$ref": "#/$defs/Item"
      },
      "title": "Items",
      "type": "array"
    }
  },
  "required": [
    "id",
    "items"
  ],
  "title": "Order",
  "type": "object"
}
"""