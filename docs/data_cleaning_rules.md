# Data Cleaning Rules

## Purpose

This document defines the preprocessing rules used to transform raw LabVIEW (.lvm) files into a clean dataset suitable for storage in PostgreSQL and downstream analytics.

---

## Cleaning Workflow

| Step | Rule | Reason |
|------|------|--------|
| 1 | Read raw `.lvm` file | Source measurement format |
| 2 | Extract metadata from file header | Capture experiment information where required |
| 3 | Skip LabVIEW header rows | Metadata is not sensor data |
| 4 | Read the sensor measurement table | Extract usable observations |
| 5 | Remove ignored sensor columns | Reduce unnecessary data |
| 6 | Rename columns using project naming convention | Improve readability and consistency |
| 7 | Apply engineering unit conversions | Standardise measurements |
| 8 | Add `fault_type` from the folder name | Identify operating condition |
| 9 | Add `run_number` from the filename | Track individual experiments |
| 10 | Add `source_file` | Support traceability |
| 11 | Add `ingestion_timestamp` | Record when the file entered the platform |
| 12 | Validate data types and missing values | Improve data quality before loading |
| 13 | Load cleaned dataset into PostgreSQL | Prepare data for analytics |

---

## Future Enhancements

- Automatic schema validation
- Duplicate file detection
- Data quality reports
- Logging and error handling