import os
from src.lib.plotting import plot_events, show_plots
from src.lib.reader import read_csv
from src.validate import validate_events



def main():
    data_files = os.listdir("./data")

    plots = {}
    for file in data_files:
        print(f"Validating {file}")
        events = list(read_csv(f"./data/{file}"))

        failed_events = validate_events(events)
        plots[file] = plot_events(events, failed_events)

    show_plots(plots)


if __name__ == "__main__":
    main()
