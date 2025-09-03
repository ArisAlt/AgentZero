# AgentZero
Version: 0.3.0
Path: /workspace/AgentZero

Cron-ready pipeline that ingests marketplace listings and design trends, analyzes them, summarizes with an LLM, and exports HTML and CSV reports.

## Project layout
- `VERSION` – stores the current semantic version.
- `src/`
  - `ingest.py` – collects Etsy listings plus Printables and Thingiverse trends.
  - `analyze.py` – computes simple metrics like counts and average price.
  - `llm.py` – placeholder LLM summary generator.
  - `report.py` – writes HTML and CSV reports.
  - `pipeline.py` – orchestrates all steps; entry point for cron.

## Data sources
- **Etsy**: titles, tags, price, favorites, review counts & dates, images, shop age.
- **Printables** and **Thingiverse**: popularity via likes/downloads to spot design trends.

## Usage
Run the pipeline once:

```bash
python -m src.pipeline
```

Reports are written to `reports/<timestamp>/`.

## Cron
Schedule daily execution at 2am:

```
0 2 * * * cd /workspace/AgentZero && /usr/bin/python -m src.pipeline >> cron.log 2>&1
```
