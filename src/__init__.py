"""Core package for AgentZero.

Version: 0.3.0
Path: src/__init__.py
"""

from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent
__version__ = (BASE_PATH / "VERSION").read_text().strip()

__all__ = ["__version__", "BASE_PATH"]
