# Project Requirements

## Project Name

Digital Twin Data Platform

---

## Objective

Design and implement an end-to-end data engineering platform capable of automatically ingesting, processing and visualising Digital Twin sensor data.

---

## Data Source

Raw LabVIEW Measurement (.lvm) files generated from a Digital Twin hydraulic system.

---

## Operating Conditions

- Healthy
- Leaking Pipe
- Clogged Injector
- Degraded Pump
- Stuck Shutoff Valve
- Faulty Pipe

Each condition contains five experimental runs.

---

## Functional Requirements

The platform shall:

- Read raw .lvm files
- Remove unnecessary metadata
- Rename sensor columns
- Apply engineering unit conversions
- Load cleaned data into PostgreSQL
- Transform data using dbt
- Automate workflows using Kestra
- Produce Power BI dashboards

---

## Non-Functional Requirements

- Modular
- Reproducible
- Containerised
- Well documented
- Easy to maintain