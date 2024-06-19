#!/user/bin/python3
""" filter_datum module """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Filter the message"""
    for field in fields:
        pattern = rf'({field}=)([^{separator}]*)'
        message = re.sub(pattern, rf'\1{redaction}', message)
    return message
