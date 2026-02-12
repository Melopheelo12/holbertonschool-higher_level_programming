#!/usr/bin/python3
"""Module to serialize and deserialize Python dictionaries to/from XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file"""
    root = ET.Element("data")  # Create root element

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)  # Create a child element for each key
        child.text = str(value)  # Store the value as text

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file back into a Python dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            result[child.tag] = child.text  # Convert text to string (default)
        return result
    except (ET.ParseError, FileNotFoundError):
        return {}
