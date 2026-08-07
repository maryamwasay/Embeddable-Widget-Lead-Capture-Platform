import requests

from app.config import settings


def get_location(ip: str):

    # Local development fallback
    if ip in ["127.0.0.1", "::1", "localhost"]:
        return {
            "country": "Local Development",
            "city": "Localhost",
        }

    providers = [
        f"{settings.GEO_PROVIDER_1}/{ip}",
        f"{settings.GEO_PROVIDER_2}/{ip}",
    ]

    for provider in providers:

        try:

            response = requests.get(
                provider,
                timeout=5,
            )

            if response.status_code == 200:

                data = response.json()

                return {
                    "country": data.get("country"),
                    "city": data.get("city"),
                }

        except Exception:
            continue

    return {
        "country": "Unknown",
        "city": "Unknown",
    }