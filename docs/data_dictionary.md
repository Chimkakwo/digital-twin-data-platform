# Data Dictionary

## Purpose

This document describes the sensor measurements contained within the Digital Twin hydraulic system dataset. It serves as the reference document for all ingestion, transformation, database modelling, and reporting activities.

---

## Dataset Overview

- **Source:** LabVIEW Measurement (.lvm) files
- **System:** Digital Twin Hydraulic Test Rig
- **Operating Conditions:**
  - Healthy
  - Leaking Pipe
  - Clogged Injector
  - Degraded Pump
  - Stuck Shutoff Valve
  - Faulty Pipe

Each operating condition contains five experimental runs.

---

## Sensor Dictionary

| Column | Clean Name | Unit | Description | Notes |
|---------|------------|------|-------------|------|
| 1 | elapsed_time | seconds | Time elapsed during the experiment | Each experiment contains approximately 60 seconds of measurements. :contentReference[oaicite:1]{index=1} |
| 2 | pressure_before_filter | bar | Pressure before the filter | Absolute pressure. :contentReference[oaicite:2]{index=2} |
| 3 | pressure_after_filter | bar | Pressure after the filter | Absolute pressure. :contentReference[oaicite:3]{index=3} |
| 4 | pressure_after_pump | bar | Pressure after the pump | Relative pressure. :contentReference[oaicite:4]{index=4} |
| 5 | pressure_after_shutoff_valve | bar | Pressure after the shut-off valve | Relative pressure. :contentReference[oaicite:5]{index=5} |
| 6 | ignored_sensor | - | Not used in the project | Ignored during ingestion. :contentReference[oaicite:6]{index=6} |
| 7 | main_flow_rate | L/min | Volumetric flow rate in the main line | :contentReference[oaicite:7]{index=7} |
| 8 | pressure_after_injector | bar | Pressure after the nozzle/injector | Relative pressure. :contentReference[oaicite:8]{index=8} |
| 9 | pump_speed | rpm | Pump rotational speed | :contentReference[oaicite:9]{index=9} |
| 10 | dpv1_opening | % | Direct Proportional Valve 1 opening | Simulates a clogged filter scenario. :contentReference[oaicite:10]{index=10} |
| 11 | dpv2_opening | % | Direct Proportional Valve 2 opening | Simulates a degraded pump scenario. :contentReference[oaicite:11]{index=11} |
| 12 | dpv3_opening | % | Direct Proportional Valve 3 opening | Simulates a stuck valve scenario. :contentReference[oaicite:12]{index=12} |
| 13 | dpv4_opening | % | Direct Proportional Valve 4 opening | Simulates a leaking pipe scenario. :contentReference[oaicite:13]{index=13} |
| 14 | dpv5_opening | % | Direct Proportional Valve 5 opening | Simulates a clogged injector scenario. :contentReference[oaicite:14]{index=14} |

---

## Notes

This document will be updated as the project progresses to include:

- PostgreSQL data types
- Engineering unit conversions
- Validation rules
- Business definitions