import argparse
import json
import yaml
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description='Konwerter plików')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    parser.add_argument('--format', type=str, choices=['json', 'yaml', 'xml'], help='Format pliku wyjściowego')
    return parser.parse_args()

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            print('Błąd: Niepoprawny format pliku JSON.')
            return None

def save_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError:
            print('Błąd: Niepoprawny format pliku YAML.')
            return None

def save_yaml_file(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def load_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError:
        print('Błąd: Niepoprawny format pliku XML.')
        return None

def save_xml_file(root, file_path):
    tree = ET.ElementTree(root)
    tree.write(file_path)

def convert_file(input_file, output_file, output_format):
    if output_format == 'json':
        data = load_json_file(input_file)
        if data is not None:
            save_json_file(data, output_file)
            print('Plik skonwertowany do formatu JSON.')
    elif output_format == 'yaml':
        data = load_yaml_file(input_file)
        if data is not None:
            save_yaml_file(data, output_file)
            print('Plik skonwertowany do formatu YAML.')
    elif output_format == 'xml':
        root = load_xml_file(input_file)
        if root is not None:
            save_xml_file(root, output_file)
            print('Plik skonwertowany do formatu XML.')
    else:
        print('Błąd: Nieobsługiwany format pliku wyjściowego.')

if __name__ == '__main__':
    args = parse_arguments()
    convert_file(args.input_file, args.output_file, args.format)

