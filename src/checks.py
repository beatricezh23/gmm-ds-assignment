
from src.lib.events import ProductionParserEvent
import numpy as np
from typing import List

"""class HistoricalData:
    def __init__(self, window_size=5):
        self.past_events = []
        self.window_size = window_size

    def add_event(self, event: ProductionParserEvent):
      #Add an event to the historical data.
        self.past_events.append(event)

    def get_rolling_data(self, mode: str) -> List[float]:
        #Get the rolling data for a specific mode.
        historical_data = [
            getattr(event.production, mode) for event in self.past_events if getattr(event.production, mode) is not None
        ]
        # Return the last `window_size` data points
        return historical_data[-self.window_size:]

    def has_enough_data(self, mode: str) -> bool:
        #Check if there is enough data for the rolling window.
        return len(self.get_rolling_data(mode)) >= self.window_size"""

def verify_total_production_above_zero(event: ProductionParserEvent) -> bool:
    if not event.production:
        return False # Production is null

    modes = event.production.get_production_modes()
    total_production = sum(getattr(event.production, mode) or 0 for mode in modes)
    return total_production > 0

"""def detect_abnormal_production(event: ProductionParserEvent, historical_data: HistoricalData, z_threshold=5) -> bool:
    production_value = getattr(event.production, mode, None)

    if production_value is None or production_value == 0:
        return True

    if not historical_data.has_enough_data(mode):
        return True

    rolling_data = historical_data.get_rolling_data(mode)
    mean_production = np.mean(rolling_data)
    std_production = np.std(rolling_data)

    if std_production == 0:
        return True

    z_score = (production_value - mean_production) / std_production

    return abs(z_score) <= z_threshold"""

def detect_missing_production_data(event: ProductionParserEvent) -> bool:
    if getattr(event.production, "coal") is None:
        return False  # if coal production mode is missing data

    return True  # no production data is missing


