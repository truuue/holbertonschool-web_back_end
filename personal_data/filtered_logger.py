#!/user/bin/python3
""" filter_datum module """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Filter the message by replacing the words in fields with the redaction
    Args:
        fields: a list of fields to replace in the message
        redaction: a string representing the redacted message
        message: a string representing the log line
        separator: a string representing the separator of fields
    Returns:
        a string representing the log line
    """
    textSplit = message.split(separator)
    for field in fields:
        for info in textSplit:
            if re.search(field, info):
                message = re.sub(info.split("=")[1], redaction, message)
    return message
