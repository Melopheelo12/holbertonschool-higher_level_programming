#!/usr/bin/env python3
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            target = "{" + key + "}"
            processed_template = processed_template.replace(target, str(value))
        
        filename = f"output_{index}.txt"
        
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists. Overwriting...")

        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
