#!/usr/bin/env python3
""" filter_datum module """
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the record """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def filter_datum(
        fields: List[str],
        redaction: str, message: str, separator: str) -> str:
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
    pattern = '|'.join([f"{field}=.*?(?={separator}|$)" for field in fields])
    return re.sub(
        pattern, lambda m: f"{m.group().split('=')[0]}={redaction}", message)


def get_logger():
    """ Get logger function """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


PII_FIELDS = ("name", "email", "phone_number", "address", "credit_card_number")
