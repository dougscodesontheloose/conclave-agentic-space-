# Data Pipeline Standard Operating Procedure (SOP)

This protocol defines the strict pipeline the Data Ops squad must follow to ensure data integrity, reproducibility, and high-quality outputs.

## Phase 1: Ingestion & Creation
- **Actor:** Senior Data Scientist
- **Action:** Identify data sources (CSV, JSON, APIs, DBs). Write automated Python scripts to ingest data.
- **Rule:** Never modify the original source file. All ingestion must save a raw timestamped copy to a local `data/raw/` directory.

## Phase 2: Cleaning & Standardization
- **Actor:** Senior Data Scientist
- **Action:** Execute programmatic cleaning via Python (Pandas). Handle nulls, format dates uniformly (ISO 8601), standardize string casing, and remove absolute outliers based on statistical rules.
- **Rule:** Document every cleaning decision. If a row is dropped, log *why* it was dropped. Save the output to `data/clean/`.

## Phase 3: Manipulation & Engineering
- **Actor:** Senior Data Scientist / Senior Data Analyst
- **Action:** Create new calculated features, perform joins across datasets, and aggregate metrics. The Scientist handles complex algorithmic engineering; the Analyst handles business-logic aggregations via SQL/Advanced Excel.
- **Rule:** Code must be modular. SQL queries must use CTEs for readability.

## Phase 4: Packaging (Envelopamento)
- **Actor:** Senior Data Analyst
- **Action:** Structure the final clean data into optimized models ready for BI tools (Star Schema, Snowflake). Design the visual hierarchy for PowerBI or Tableau.
- **Rule:** The data model must support rapid filtering and dynamic calculations (DAX/LOD). No complex transformations should happen in the BI layer if they can be done in the DB/Python layer.

## Phase 5: Delivery & Translation
- **Actor:** Senior Data Analyst
- **Action:** Apply the `data-translation-system.md` protocol. Deliver the final dashboard, report, or executive summary to the stakeholder.
- **Rule:** The delivery must not just be "data"; it must be an answer to a business question.
