import sys
import os
import json
import yaml
import xml.etree.ElementTree as ET

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
        return None, None

def load_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root, tree

def load_json_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data, None

def load_yaml_file(file_path):
    with open(file_path) as file:
        data = yaml.safe_load(file)
    return data, None

def save_file(data, file_path, tree=None):
    _, file_extension = os.path.splitext(file_path)

    if file_extension == '.xml':
        save_xml_file(data, file_path, tree)
    elif file_extension == '.json':
        save_json_file(data, file_path)
    elif file_extension == '.yml' or file_extension == '.yaml':
        save_yaml_file(data, file_path)
    else:
        print("Unsupported file format")

def save_xml_file(root, file_path, tree=None):
    if tree is None:
        tree = ET.ElementTree(root)
    tree.write(file_path)

def save_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def save_yaml_file(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def convert_file(input_file_path, output_file_path):
    data, tree = load_file(input_file_path)
    if data is not None:
        save_file(data, output_file_path, tree)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    convert_file(input_file_path, output_file_path)
