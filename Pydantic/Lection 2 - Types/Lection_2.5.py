# Unions

from pydantic import BaseModel


class Car(BaseModel):
    make: str
    model: str
    seat_count: int


class Motorcycle(BaseModel):
    make: str
    model: str
    has_sidecar: bool


class Truck(BaseModel):
    make: str
    model: str
    payload_capacity: float


from typing import Union


# Here we will use the flexible data type Union!
class Vehicle(BaseModel):
    owner: str
    vehicle_details: Union[Car, Motorcycle, Truck]


example_1 = Vehicle(owner="Sow", vehicle_details=Car(make="BMW", model="S",
                                           seat_count=5))

example_2 = Vehicle(owner="Davyd", vehicle_details=Motorcycle(make="HD", model="Softail",
                                                  has_sidecar=False))

print(example_1)
print(example_2)

#Because of UNION we have no problem here!
#The order in the Union[Car, Motorcycle, Truck] is important
#We have to create exemplar of Vehicle in this order!




#DRY case!
class VehicleBase(BaseModel):
    make: str
    model: str

class Car(VehicleBase):
    seat_count: int


class Motorcycle(VehicleBase):
    has_sidecar: bool


class Truck(VehicleBase):
    payload_capacity: float
