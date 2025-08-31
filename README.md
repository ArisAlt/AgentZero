# AgentZero
Version: 0.1.0
Path: /workspace/AgentZero

Project layout:
- `VERSION` – stores the current semantic version.
- `src/data_sources/` – integrations for Etsy, Printables/Thingiverse, eBay/Amazon, and CSV importers.
- `src/signals/` – processes favorites, reviews, listing age, and price/shipping.
- `src/analytics/` – velocity calculations, MoM trends, clustering, and gap mining.
- `src/ideation/` – LLM-driven model specification engine.

## FIND WHAT SELLS
We collect marketplace signals such as titles, tags, price, favorites, reviews, images, and shop age. Data sources include Etsy,
 Printables/Thingiverse, eBay/Amazon, eRank, Alura, Marmalead, JungleScout, and Helium10.

### Sales Velocity
Track listing order counts to gauge daily traction.

### MoM Trend
Compare month-over-month changes to spot emerging demand.

### Price Bands
Segment listings into price tiers to detect under- or over-served ranges.

### Theme Clusters
Group listings by recurring concepts to highlight popular themes.

## SUGGEST NEW MODELS
Trend gaps and review complaints feed into model specifications detailing the problem statement, variants, printability, bill of
 materials and packaging, and a photoshoot list.

### Gap Mining
Use demand-supply differences to pinpoint unmet needs.

### Ideation Engine (LLM with guardrails)
Generate model concepts with constraints to ensure practical, printable designs.
