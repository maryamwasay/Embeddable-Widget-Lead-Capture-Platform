from app.services.email_service import (
    send_confirmation_email
)


def test_send_email():

    result = send_confirmation_email(
        "john@test.com",
        "John"
    )

    assert result is True