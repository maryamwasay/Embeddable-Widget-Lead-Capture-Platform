from cachetools import TTLCache


class CacheService:
    """
    Simple in-memory cache.
    Items expire automatically after the TTL.
    """

    widget_cache = TTLCache(
        maxsize=1000,
        ttl=300
    )  # 5 minutes

    geo_cache = TTLCache(
        maxsize=1000,
        ttl=86400
    )  # 24 hours

    @classmethod
    def get_widget(cls, widget_id: int):
        return cls.widget_cache.get(widget_id)

    @classmethod
    def set_widget(cls, widget_id: int, data):
        cls.widget_cache[widget_id] = data

    @classmethod
    def get_geo(cls, ip_address: str):
        return cls.geo_cache.get(ip_address)

    @classmethod
    def set_geo(
        cls,
        ip_address: str,
        location: dict
    ):
        cls.geo_cache[ip_address] = location

    @classmethod
    def clear_widget_cache(cls):
        cls.widget_cache.clear()

    @classmethod
    def clear_geo_cache(cls):
        cls.geo_cache.clear()
