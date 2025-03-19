#For Better Performance: Literals

#Nowadays Literals better than Enum if we want to create limited data in others cases better to use enum!

from enum import Enum
from pydantic import BaseModel, ValidationError

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

class ItemWithEnum(BaseModel):
    name: str
    color: Color

try:
    item = ItemWithEnum(name = "Chair", color = "red")
    print(item)
except ValidationError as e:
    print(e)



from typing import Literal

# Literal["a", "b", "c"] -> Literals

class ItemWithLiteral(BaseModel):
    name: str
    color: Literal["red", "green", "blue"]

try:
    #item = ItemWithEnum(name = "Chair", color = "grey") #Error
    item = ItemWithLiteral(name="Chair", color="grey") #Error as well
    print(item)
except ValidationError as e:
    print(e)



from pydantic import TypeAdapter
literal = Literal["red", "green", "blue"]

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

lit_adapter = TypeAdapter(literal)
enum_adapter = TypeAdapter(Color)


from timeit import timeit

res1 = timeit(lambda: lit_adapter.validate_python("red"), number=10000)
res2 = timeit(lambda: enum_adapter.validate_python("red"), number=10000)
print('res 1 = {res1}', format(res1))
print('res 2 = {res2}', format(res2))
print(res1/res2) #ratio = 0.985

#res 1 = {res1} 2.494353416841477
#res 2 = {res2} 2.3749498748220503