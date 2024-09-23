
from src.lib.events import ProductionParserEvent


def verify_total_production_above_zero(event: ProductionParserEvent) -> bool:
    if not event.production:
        return False # Production is null

    modes = event.production.get_production_modes()
    total_production = sum(getattr(event.production, mode) or 0 for mode in modes)
    return total_production > 0
