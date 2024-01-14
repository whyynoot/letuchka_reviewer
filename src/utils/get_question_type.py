import re

def get_question_type(input_string: str) -> str:
    match = re.search(r'\((.*?)\)', input_string)
    if match:
        return match.group(1)
    return ''