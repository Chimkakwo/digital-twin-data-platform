# Digital Twin Data Platform

## Overview

The Digital Twin Data Platform is an end-to-end data engineering project developed using industrial sensor data collected from a Digital Twin hydraulic system.

The project demonstrates how raw LabVIEW Measurement (.lvm) files can be automatically ingested, cleaned, transformed, stored, and visualised using modern data engineering tools.

Rather than relying on already prepared datasets, this project begins with raw industrial measurement files and builds a complete data pipeline from data acquisition through to business intelligence dashboards.

---

## Business Problem

Industrial equipment continuously generates large volumes of sensor data. These measurements are often exported in proprietary formats such as LabVIEW Measurement (.lvm), making them difficult to analyse directly.

This project automates the ingestion and transformation of these files to provide reliable and repeatable analytics for equipment health monitoring and fault analysis.

---

## Dataset

The dataset contains six operating conditions:

- Healthy
- Leaking Pipe
- Clogged Injector
- Degraded Pump
- Stuck Shutoff Valve
- Faulty Pipe

Each operating condition contains five experimental runs captured from multiple sensors.

---

## Technology Stack

- Python
- Docker
- PostgreSQL
- Kestra
- dbt
- Power BI
- Git & GitHub
- Google Drive API

---

## Planned Architecture

```text
LabVIEW (.lvm)
        │
        ▼
Google Drive
        │
        ▼
Python ETL
        │
        ▼
PostgreSQL
        │
        ▼
dbt
        │
        ▼
Power BI
```

---

## Project Status

🚧 Currently under development.

The project is being built incrementally following software engineering and data engineering best practices.
