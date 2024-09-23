import csv
from collections.abc import Iterator
from src.lib.events import PowerBreakdown, ProductionParserEvent
from datetime import datetime


def read_csv(path: str) -> Iterator[ProductionParserEvent]:
    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            event = ProductionParserEvent(
                created_at=datetime.strptime(
                    row["created_at"], "%Y-%m-%d %H:%M:%S.%f %z"
                ),
                updated_at=datetime.strptime(
                    row["updated_at"], "%Y-%m-%d %H:%M:%S.%f %z"
                ),
                datetime=datetime.strptime(row["datetime"], "%Y-%m-%d %H:%M:%S.%f %z"),
                zone_key=row["zone_key"],
                source=row["source"],
                production=PowerBreakdown.from_string(row["production"]),
            )
            yield event
