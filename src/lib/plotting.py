from datetime import datetime, timedelta
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from src.lib.events import ProductionParserEvent, PowerBreakdown

MODE_COLORS = {
    "wind": "#74cdb9",
    "solar": "#f27406",
    "hydro": "#2772b2",
    "biomass": "#166a57",
    "geothermal": "yellow",
    "nuclear": "#AEB800",
    "gas": "#bb2f51",
    "coal": "#ac8c35",
    "oil": "#867d66",
    "unknown": "lightgray",
}


def plot_events(
    events: list[ProductionParserEvent],
    error_events: list[tuple[datetime, str]] | None = None,
):
    fig = go.Figure()
    non_null_events = [event for event in events if event.production]

    for mode in PowerBreakdown.get_production_modes():
        fig.add_trace(
            go.Scatter(
                x=[event.datetime for event in non_null_events],
                y=[getattr(event.production, mode) for event in non_null_events],
                name=mode,
                stackgroup="one",
                fillcolor=MODE_COLORS[mode],
                line={"width": 0},
            )
        )

    if error_events:
        for error_event in error_events:
            fig.add_trace(
                go.Scatter(
                    x=[error_event[0]],
                    y=[0],
                    mode="markers",
                    name=error_event[1],
                    marker={"color": "red", "size": 10, "symbol": "x"},
                    showlegend=False,
                )
            )
            fig.add_vrect(
                x0=error_event[0] - timedelta(minutes=30),
                x1=error_event[0] + timedelta(minutes=30),
                fillcolor="LightSalmon",
                opacity=0.5,
                layer="above",
                line_width=0,
            )
    return fig


def show_plots(plots: dict[str, go.Figure]):
    fig = make_subplots(rows=len(plots), cols=1, subplot_titles=list(plots.keys()))
    for i, (file, plot) in enumerate(plots.items()):
        for trace in plot.data:
            if i != 0:  # only show legend for first plot
                trace.showlegend = False

            fig.add_trace(trace, row=i + 1, col=1)

        for vrect in plot.layout.shapes:
            fig.add_shape(vrect, row=i + 1, col=1)

    for i in range(1, len(plots) + 1):
        fig.update_yaxes(title_text="Production (MW)", row=i, col=1)

    fig.update_layout(hoverlabel_namelength=-1)
    fig.show()
