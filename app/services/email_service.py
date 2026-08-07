import logging

from app.config import settings


logger = logging.getLogger(__name__)


def send_confirmation_email(
    recipient_email: str,
    name: str
):
    """
    Sends confirmation email.

    In this capstone version:
    We simulate email sending by logging it.

    A real SMTP provider can replace this later.
    """

    try:

        message = (
            f"Confirmation email sent to {recipient_email} "
            f"for {name}"
        )

        logger.info(message)


        return True


    except Exception as e:

        # Important:
        # Email failure should NEVER break submission flow.

        logger.error(
            f"Email sending failed: {str(e)}"
        )

        return False