"""Analysis module.

Version: 0.3.0
Path: src/analyze.py
"""

from statistics import mean
from typing import Any, Dict, List


def analyze(data: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    """Compute simple metrics from ingested data."""
    etsy = data.get("etsy", [])
    prices = [item.get("price", 0.0) for item in etsy]
    metrics: Dict[str, Any] = {
        "etsy_count": len(etsy),
        "etsy_avg_price": round(mean(prices), 2) if prices else 0.0,
        "printables_count": len(data.get("printables", [])),
        "thingiverse_count": len(data.get("thingiverse", [])),
    }
    return metrics
