# Personal Agent Cortisol Circadian CAR Curve Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Cortisol Awakening Response (CAR) area-under-curve modeler, Diurnal Cortisol Slope (DCS) flattener detector, and hypothalamic-pituitary-adrenal (HPA) axis stabilizer.

## Architecture

```mermaid
flowchart TD
    SalivarySamples[Multi-Point Free Cortisol Samples nmol/L] --> CAREngine[CAR & Diurnal Curve Engine]
    CAREngine --> CARPeak[CAR 30-min Surge Percentage: Blunted vs Hyper]
    CAREngine --> DCSSlope[Diurnal Slope Decay: Steep vs Flat Burnout]
    CAREngine --> NocturnalNadir[Evening Nadir Clearance: Under 3.5 nmol/L]
    CARPeak & DCSSlope & NocturnalNadir --> HPAProtocols[Phased Morning Light & Evening GABAergic Protocols]
```

## Quickstart

```python
from client import PersonalAgentCortisolCircadianCarCurve

agent = PersonalAgentCortisolCircadianCarCurve()
res = agent.evaluate_diurnal_cortisol_curve([{"minutes_post_wake": 0, "nmol_l": 12.0}, {"minutes_post_wake": 30, "nmol_l": 22.0}])
print(f"CAR Rise: {res['car_magnitude_rise_pct']} | Status: {res['car_functional_status']}")
```
