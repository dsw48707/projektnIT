import argparse
import json
import yaml
import xmltodict
import xml.etree.ElementTree as ET

 parser = argparse.ArgumentParser(description='konwerter')

    parser.add_argument('input_file', help='plik wejściowy')
    parser.add_argument('output_file', help='plik wyjściowy')
    parser.add_argument('format', type=str, help='Format pliku')

    args = parser.parse_args()
    
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
 
 
