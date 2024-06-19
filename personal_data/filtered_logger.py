#!/user/bin/python3
import re


def filter_datum(fields, redaction, message, separator):
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
    pattern = '|'.join([f"{field}=[^\\{separator}]*" for field in fields])
    return re.sub(pattern, f"{redaction}", message)
