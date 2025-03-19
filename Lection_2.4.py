#Sets and Tuples

from pydantic import BaseModel, Field, ValidationError
from typing import Set

class UniqueNumbers(BaseModel):
    values: Set[int] = Field(max_items = 10, min_items = 2)

try:
    unique_numbers = UniqueNumbers(values= {1,2,3,4,'4'}) #values={1, 2, 3, 4}
    print(unique_numbers)
except ValidationError as e:
    print(e)


from typing import Tuple
class Coordinates(BaseModel):
    point : Tuple[float, float, float]

coordinates = Coordinates(point=(1.0, 2.0, 3.0))
print(coordinates) #point=(1.0, 2.0, 3.0)



class UserInfo(BaseModel):
    details : Tuple[int, str, bool]

user_info = UserInfo(details=(42,'Answer',True))
print(user_info) # details=(42, 'Answer', True)


#Tuple with undefined length
class GroceryList(BaseModel):
    items: Tuple[str, ...]

grocery_list = GroceryList(items = ("apples",)) #items=('apples',) -> There is will be
#A mistake if we put just ("apples")!
print(grocery_list)