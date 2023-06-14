import argparse
import json
import yaml
import xmltodict

 parser = argparse.ArgumentParser(description='konwerter')

    parser.add_argument('input_file', help='plik wejściowy')
    parser.add_argument('output_file', help='plik wyjściowy')
    parser.add_argument('format', type=str, help='Format pliku')

    args = parser.parse_args()
