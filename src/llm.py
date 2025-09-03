"""LLM summarization module.

Version: 0.3.0
Path: src/llm.py
"""

from typing import Dict, Any


def generate_summary(analysis: Dict[str, Any]) -> str:
    """Generate a text summary from analysis results.

    This is a placeholder for an actual LLM call.
    """
    return (
        "Found {etsy_count} Etsy listings (avg price ${etsy_avg_price}), "
        "{printables_count} Printables designs and {thingiverse_count} "
        "Thingiverse designs.".format(**analysis)
    )
