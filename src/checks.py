
from src.lib.events import ProductionParserEvent
import numpy as np

def verify_total_production_above_zero(event: ProductionParserEvent) -> bool:
    if not event.production:
        return False # Production is null

    modes = event.production.get_production_modes()
    total_production = sum(getattr(event.production, mode) or 0 for mode in modes)
    return total_production > 0

def detect_abnormal_production(event: ProductionParserEvent, mode: str, past_events: list, window_size=5, z_threshold=10) -> bool:
    production_value = getattr(event.production, mode, None)

    if production_value is None:
        return True

    if production_value == 0:
        return True

    historical_data = [getattr(past_event.production, mode) for past_event in past_events if getattr(past_event.production, mode) is not None]

    if len(historical_data) < window_size:
        return False  # not enough data for the rolling window

    rolling_data = historical_data[-window_size:]
    mean_production = np.mean(rolling_data)
    std_production = np.std(rolling_data)

    if std_production == 0:
        return True

    z_score = (production_value - mean_production) / std_production
    if abs(z_score) > z_threshold:
        return False  # abnormal production detected

def detect_missing_production_data(event: ProductionParserEvent) -> bool:
    if getattr(event.production, "coal") is None:
        return False  # if coal production mode is missing data

    return True  # no production data is missing


