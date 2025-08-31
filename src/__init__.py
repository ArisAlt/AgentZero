"""Core package for AgentZero."""

from pathlib import Path

__all__ = ["__version__"]

__version__ = (Path(__file__).resolve().parent.parent / "VERSION").read_text().strip()
