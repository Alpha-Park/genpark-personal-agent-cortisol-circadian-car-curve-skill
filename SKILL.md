---
name: genpark-personal-agent-cortisol-circadian-car-curve-skill
version: "1.0.0"
description: "Zero-dependency Cortisol Awakening Response (CAR) area-under-curve modeler, Diurnal Cortisol Slope (DCS) flattener detector, and hypothalamic-pituitary-adrenal (HPA) axis stabilizer."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Cortisol Circadian CAR Curve Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to track human stress resilience, model the 30-minute Cortisol Awakening Response (CAR), detect pathological diurnal cortisol slope flattening, and protect evening nadir descent.

## Agent In-Context Capabilities

- **CAR Peak Quantification**: Distinguishes healthy 50-100% awakening surges from burned-out blunted responses or anxiety-driven hyper-reactivity.
- **Diurnal Slope Decay Tracking**: Monitors hourly clearance rate to identify systemic fatigue, chronic low-grade neuroinflammation, or adrenal burnout.
- **Targeted HPA Protocol Synthesis**: Pairs morning light/cold anchors with evening GABAergic down-regulation to reconstruct steep biological rhythms.

## Tools Summary

1. `evaluate_diurnal_cortisol_curve`: Computes waking, peak, and evening values, slope per hour, and clinical status.
2. `recommend_hpa_resilience_protocol`: Prescribes morning entrainment and evening calming interventions.
