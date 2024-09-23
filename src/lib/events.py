from abc import ABC
from dataclasses import dataclass
from typing import NamedTuple
from datetime import datetime

class PowerBreakdown(NamedTuple):
    # The order of the fields, match the order of the fields in the database
    biomass: float | None = None
    coal: float | None = None
    gas: float | None = None
    geothermal: float | None = None
    hydro: float | None = None
    nuclear: float | None = None
    oil: float | None = None
    solar: float | None = None
    unknown: float | None = None
    wind: float | None = None
    battery_storage: float | None = None
    hydro_storage: float | None = None

    @classmethod
    def get_production_modes(cls) -> tuple[str, ...]:
        return cls._fields[:10]

    @classmethod
    def get_storage_modes(cls) -> tuple[str, ...]:
        return cls._fields[10:]


    @classmethod
    def from_string(cls, tuple_str: str) -> "PowerBreakdown":
        def parse_float_or_none(value: str) -> float | None:
            return None if value == "" else float(value)
        cleaned_str = tuple_str.removeprefix("(").removesuffix(")")
        return cls(*map(parse_float_or_none, cleaned_str.split(',')))

@dataclass(frozen=True, slots=True)
class ParserEvent(ABC):
    created_at: datetime
    updated_at: datetime
    datetime: datetime
    zone_key: str
    source: str

@dataclass(frozen=True, slots=True)
class ProductionParserEvent(ParserEvent):
    production: PowerBreakdown | None = None
    capacity: PowerBreakdown | None = None
