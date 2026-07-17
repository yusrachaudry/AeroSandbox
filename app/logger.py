# app/logger.py

import csv
import os
from datetime import datetime

FILE_NAME = "data/results.csv"


def initialize_csv():
    """Create the CSV file if it doesn't already exist."""

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Participant",
                "Scenario",
                "Decision",
                "Confidence",
                "Timestamp"
            ])


def save_result(participant, scenario, decision, confidence):
    """Save one participant's response."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            participant,
            scenario,
            decision,
            confidence,
            timestamp
        ])