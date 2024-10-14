from datetime import datetime
from src.checks import verify_total_production_above_zero
from src.checks import detect_abnormal_production
from src.checks import detect_missing_production_data
from src.lib.events import ProductionParserEvent


CHECKS_TO_RUN = [verify_total_production_above_zero, detect_missing_production_data, detect_missing_production_data]

def is_event_valid(event: ProductionParserEvent) -> tuple[bool, list[str]]:
    failed_checks = []
    for check in CHECKS_TO_RUN:
        if not check(event):
            failed_checks.append(check.__name__)

    production_modes = event.production.get_production_modes()
    for mode in production_modes:
    if not detect_abnormal_production(event, mode):
        failed_checks.append(f"abnormal_{mode}_production")

    return len(failed_checks) == 0, failed_checks

def validate_events(events: list[ProductionParserEvent]) -> list[tuple[datetime, str]]:
    failed_events = []
    for event in events:
        is_valid, failed_checks = is_event_valid(event)
        if not is_valid:
            failed_events.append((event.datetime, ", ".join(failed_checks)))

    return failed_events