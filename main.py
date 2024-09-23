import os
from src.lib.plotting import plot_events
from src.lib.reader import read_csv
from src.validate import validate_events
from plotly.subplots import make_subplots


def main():
    data_files = os.listdir("./data")

    plots = {}
    for file in data_files:
        print(f"Validating {file}")
        events = list(read_csv(f"./data/{file}"))

        failed_events = validate_events(events)
        plots[file] = plot_events(events, failed_events)

    fig = make_subplots(rows=len(plots), cols=1, subplot_titles=list(plots.keys()))
    for i, (file, plot) in enumerate(plots.items()):
        for trace in plot.data:
            if i != 0:  # only show legend for first plot
                trace.showlegend = False

            fig.add_trace(trace, row=i + 1, col=1)

        for vrect in plot.layout.shapes:
            fig.add_shape(vrect, row=i + 1, col=1)

    fig.show()


if __name__ == "__main__":
    main()
