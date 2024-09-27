# Data Science - Take home assignment

Welcome to the Electricity Maps Data Science technical challenge!

First off, thanks for taking the time and putting effort into completing this challenge, we really appreciate it!

## Task

At Electricity Maps, we ingest data from 100s of regions around the world. Sometimes data sources report incorrect data, and we need automated ways to detect these errors. You task is to implement data quality checks that are able to catch some of these errors.

The data you will be working with is a timeseries of electricity production breakdowns. Each event represents the electricity produced by different technologies in a region at a given time. We have included data from 3 different regions that each includes a different data quality issue.

## Data
#### DK-DK1
This dataset contains data from West Denmark and includes a few hours of zero production. The data quality check to flag these datapoints have already been implemented and you can use this as a reference for the other datasets.
![DK-DK1 data](./.github/figures/DK-DK1.png)

#### FR
This dataset contains data from France and includes a few hours of abnormaly high wind production. The data quality check to flag these datapoints have not been implemented and you will need to implement this yourself.
![FR data](./.github/figures/FR.png)

#### DE
This dataset contains data from Germany and includes a few hours of incomplete data. Coal production have not been reported for a few hours. The data quality check to flag these datapoints have not been implemented and you will need to implement this yourself.
![DE data](./.github/figures/DE.png)

## Setup

This repository contains a very simple data quality pipeline that:
1. Reads data from the CSV files
2. Runs a list of data quality checks
3. Outputs plots showing the flagged data points

## Get started

Step 1: Create a new repo from this template and make it private.
👇
![copy template](./.github/figures/template.png)

Step 2: Clone it locally and get the project up and running.

Create a virtual environment and install the dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Step 3: Run the pipeline
```bash
python main.py
```

## Deliverables

1. Implement data quality checks in `src/checks.py` and add them to the list of checks in `src/validate.py`
2. Run the pipeline using `python main.py` and verify that the checks are working as expected
3. Replace this README with a description of how you solved the task. Explain your thought process and the decisions you made along the way. Also include any improvements you would make if you had more time.
4. Share the repository with [@FelixDQ](https://github.com/FelixDQ), [@pierresegonne](https://github.com/pierresegonne) and [@wobniarin](https://github.com/wobniarin)

## Notes

- Spend no more than 3 hours on this task
- We included an investigation notebook (`investigation.ipynb`) that you can use to explore the data
- You are free to make any changes to the pipeline, but with the limited time, we recommend focusing on the data quality checks
- If you use any static or external data, please include your thoughts on how we could apply this to other regions. When maintaining 100s of regions, we want the checks to be as general as possible.
- Feel free to reach out to us if you have any questions
- Have fun and remember that there is no single correct answer to this task.

