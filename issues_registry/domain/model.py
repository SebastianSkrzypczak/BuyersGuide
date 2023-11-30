from dataclasses import dataclass


@dataclass
class Car:
    type: str
    brand: str
    model: str
    year: str
    fuel: str
    engine_displacement: str
    issues: list[Issue]
