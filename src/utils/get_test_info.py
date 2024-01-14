import re
import os

def get_test_info(input_string: str) -> str:
    match = re.search(r'(.*?)_(.*?)\.xlsx$', os.path.basename(input_string))
    if match:
        return match.group(1), match.group(2)
    return ''