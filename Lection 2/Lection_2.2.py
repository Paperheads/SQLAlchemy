# Lists and Nested Lists
import pydantic
from pydantic import BaseModel
from typing import List


class ShoppingList(BaseModel):
    items: List[str]  # Each object must be string


try:
    shopping_list = ShoppingList(items=['apple',
                                        'banana',
                                        'cherry'])
    print(shopping_list)
except pydantic.ValidationError as e:
    print(e)

# Additional Req

from pydantic import Field


class ShoppingList(BaseModel):
    items: List[str] = Field(max_items=5, min_items=2)


try:
    shopping_list = ShoppingList(items=['apple',
                                        'apple',
                                        'apple',
                                        'apple'])
    print(shopping_list)
except pydantic.ValidationError as e:
    print(e)


class Matrix(BaseModel):
    grid: List[List[int]]  # Nested list


try:
    matrix = Matrix(grid=[[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])
    print(matrix)
except pydantic.ValidationError as e:
    print(e)



#Last example
class Ingredient(BaseModel):
    name: str
    quantity: float

#The type of the requirments can be the type we defined
class Recipe(BaseModel):
    ingredients: List[Ingredient]

try:
    recipe = Recipe(ingredients=[
        Ingredient(name='apple', quantity=5.0),
        Ingredient(name='banana', quantity=3.0),
        Ingredient(name='cherry', quantity=2.5),
        Ingredient(name='salt', quantity=0.6),
    ])

    print(recipe)
except pydantic.ValidationError as e:
    print(e)
