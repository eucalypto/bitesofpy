import re


def validate_license(key: str) -> bool:
    """Validates license key according to this format: PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)

    :param key: key to be validated
    :type key: str

    :returns: True if matches, else False
    :rtype: bool
    """
    return re.match('^PB-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}$', key) is not None
