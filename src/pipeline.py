"""Pipeline entry point.

Version: 0.3.0
Path: src/pipeline.py
"""

from datetime import datetime, timezone
from pathlib import Path

from . import __version__, BASE_PATH
from .ingest import ingest
from .analyze import analyze
from .llm import generate_summary
from .report import generate_reports


def run() -> Path:
    """Execute the full data pipeline and return the output directory."""
    data = ingest()
    analysis = analyze(data)
    summary = generate_summary(analysis)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_dir = BASE_PATH / "reports" / timestamp
    generate_reports(summary, analysis, output_dir)
    print(f"AgentZero v{__version__}: report generated at {output_dir}")
    return output_dir


if __name__ == "__main__":  # pragma: no cover - cron entry point
    run()
