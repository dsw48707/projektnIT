import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import xmltodict
import xml.dom.minidom
import sys
import os

 def load_file(file_path):
    _, file_extension = os.path.splitext(file_path)

    if file_extension == '.xml':
        return load_xml_file(file_path)
    elif file_extension == '.json':
        return load_json_file(file_path)
    elif file_extension == '.yml' or file_extension == '.yaml':
        return load_yaml_file(file_path)
    else:
        print("Unsupported file format")
        return None

def load_xml_file(file_path):
    tree = ET.parse(file_path)
    return tree

def load_json_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data

def load_yaml_file(file_path):
    with open(file_path) as file:
        data = yaml.safe_load(file)
    return data

def save_file(data, file_path):
    _, file_extension = os.path.splitext(file_path)

    if file_extension == '.xml':
        save_xml_file(data, file_path)
    elif file_extension == '.json':
        save_json_file(data, file_path)
    elif file_extension == '.yml' or file_extension == '.yaml':
        save_yaml_file(data, file_path)
    else:
        print("Unsupported file format")

def save_xml_file(tree, file_path):
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def save_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def save_yaml_file(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def convert_file(input_file_path, output_file_path):
    data = load_file(input_file_path)
    if data is not None:
        save_file(data, output_file_path)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    convert_file(input_file_path, output_file_path)
