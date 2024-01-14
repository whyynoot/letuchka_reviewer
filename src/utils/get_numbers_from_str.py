import re

def extract_numbers(input_string: str) -> list:
    pattern = r'\b\d+\b'
    matches = re.findall(pattern, input_string)
    return [int(match) for match in matches]