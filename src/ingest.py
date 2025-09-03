"""Data ingestion module.

Version: 0.3.0
Path: src/ingest.py
"""

from typing import Any, Dict, List


# In production these would hit real APIs or scraping layers.

def fetch_etsy_listings() -> List[Dict[str, Any]]:
    """Fetch Etsy listings for 3D-printed goods.

    Returns a list of records with keys:
    ``title``, ``tags``, ``price``, ``favorites``, ``review_count``,
    ``review_dates``, ``image``, ``shop_age_days``.
    """
    return [
        {
            "title": "Sample 3D Printed Vase",
            "tags": ["3d printed", "vase"],
            "price": 19.99,
            "favorites": 42,
            "review_count": 10,
            "review_dates": ["2024-01-10"],
            "image": "https://example.com/vase.jpg",
            "shop_age_days": 365,
        }
    ]


def fetch_printables_trends() -> List[Dict[str, Any]]:
    """Fetch trending designs from Printables."""
    return [
        {
            "title": "Phone Holder",
            "likes": 120,
            "downloads": 400,
        }
    ]


def fetch_thingiverse_trends() -> List[Dict[str, Any]]:
    """Fetch trending designs from Thingiverse."""
    return [
        {
            "title": "Cable Organizer",
            "likes": 80,
            "downloads": 250,
        }
    ]


def ingest() -> Dict[str, List[Dict[str, Any]]]:
    """Collect data from all sources."""
    return {
        "etsy": fetch_etsy_listings(),
        "printables": fetch_printables_trends(),
        "thingiverse": fetch_thingiverse_trends(),
    }
