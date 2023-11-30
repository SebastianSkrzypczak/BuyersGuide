from dataclasses import dataclass


@dataclass
class Brand:
    id = int
    models = list


@dataclass
class Car:
    type: str
    brand: Brand
    model: Brand.model
    year: int
    fuel: str
    engine_displacement: str
    issues: list[Issue]
