# Dict

import pydantic
from pydantic import BaseModel
from typing import Dict


class UserProfiles(BaseModel):
    profiles: Dict[str, int]  # str for key and int for the value


try:
    user_profiles = UserProfiles(profiles={"alice": 25, "bob": 23})
    print(user_profiles)
except pydantic.ValidationError as e:
    print(e)

print(len(user_profiles.profiles))  # 2
print(max(user_profiles.profiles.values()))  # 25

from pydantic import Field


# additional req
class UserProfiles(BaseModel):
    profiles: Dict[str, int] = Field(min_length=2)


# More complex structure
# With Nested dict
class Product(BaseModel):
    name: str
    price: float


class ProductCatalog(BaseModel):
    products: Dict[str, Product]


try:
    catalog = ProductCatalog(
        products={
            "p1": Product(name="tea", price=4.99),
            "p2": Product(name="coffee", price=3.99),
            "p3": {"name": "pasta", "price": 13.09}
        }  # This form will work because Pydantic will shift it as our valid data
    )
    print(catalog)
except pydantic.ValidationError as e:
    print(e)


# Even more complexity example
class Order(BaseModel):
    product_id: str
    quantity: int


class OrderBook(BaseModel):
    orders: Dict[str, Dict[str, Order]]


order_book = OrderBook(
    orders={
        'o1': {'i1': Order(product_id="A1", quantity=2)}
    }
)
print(order_book)
