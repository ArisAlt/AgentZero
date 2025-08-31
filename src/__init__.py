from pathlib import Path

__all__ = ["__version__", "__version_path__"]

__version_path__ = Path(__file__).resolve().parent.parent / "VERSION"
__version__ = __version_path__.read_text().strip()
