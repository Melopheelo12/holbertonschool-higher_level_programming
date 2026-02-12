#!/usr/bin/python3
"""Module to convert CSV data to JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and save it as data.json"""
    try:
        data_list = []

        # Read CSV file
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(dict(row))

        # Write JSON data to data.json
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
