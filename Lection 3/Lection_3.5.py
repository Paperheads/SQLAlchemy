#Enumerations

'''
What are enums?

- A set of named constants
- Defined in python by sub-classing enum.Enum

'''

from enum import Enum

from pydantic import BaseModel


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

print(Color.GREEN.value) #green


class Item(BaseModel):
    name: str
    color: Color

item = Item(name = "chair", color = "red")
print(item) #name='chair' color=<Color.RED: 'red'>

item = Item(name = "chair", color = "pink")
print(item) #Input should be 'red', 'green' or 'blue' [type=enum, input_value='pink', input_type=str]


#We have several benefites while use Enums. -> Readable, better validation, strict data etc
