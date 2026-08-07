from app.services.spam_service import check_spam


def test_valid_submission():

    data = {
        "name": "John",
        "email": "john@test.com"
    }

    assert check_spam(data) is False


def test_honeypot_website():

    data = {
        "name": "John",
        "website": "spam.com"
    }

    assert check_spam(data) is True


def test_honeypot_url():

    data = {
        "url": "spam"
    }

    assert check_spam(data) is True


def test_honeypot_company():

    data = {
        "company": "spam"
    }

    assert check_spam(data) is True