import re


class Validators:

    @staticmethod
    def valid_email(email: str) -> bool:

        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        return re.match(pattern, email) is not None

    @staticmethod
    def valid_phone(phone: str | None) -> bool:

        if phone is None:
            return True

        pattern = r"^[0-9+\-\s()]{7,20}$"

        return re.match(pattern, phone) is not None

    @staticmethod
    def validate_message(message: str | None) -> bool:

        if message is None:
            return True

        return len(message) <= 1000

    @staticmethod
    def validate_name(name: str) -> bool:

        return (
            len(name.strip()) >= 2
            and len(name) <= 100
        )