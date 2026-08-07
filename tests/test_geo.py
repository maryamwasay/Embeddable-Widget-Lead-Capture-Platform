from unittest.mock import patch

from app.services.geo_service import get_location


@patch("app.services.geo_service.requests.get")
def test_geo_lookup_success(mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "country": "Pakistan",
        "city": "Lahore"
    }

    result = get_location("8.8.8.8")

    assert result["country"] == "Pakistan"
    assert result["city"] == "Lahore"


@patch("app.services.geo_service.requests.get")
def test_geo_lookup_failure(mock_get):

    mock_get.side_effect = Exception()

    result = get_location("8.8.8.8")

    assert result["country"] is None
    assert result["city"] is None