#!/user/bin/python3

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
    for field in fields:
        message = message.replace(field + separator, redaction + separator)
    return message
