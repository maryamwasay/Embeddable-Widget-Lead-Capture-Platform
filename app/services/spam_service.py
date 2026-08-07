def check_spam(data: dict) -> bool:
    """
    Honeypot spam protection.

    Real users never fill the hidden website field.
    Bots usually fill every input.
    """

    honeypot_fields = [
        "website",
        "url",
        "company"
    ]


    for field in honeypot_fields:

        value = data.get(field)


        if value:

            return True


    return False