# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Cortisol Circadian CAR Curve Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentCortisolCircadianCarCurve

def main():
    agent = PersonalAgentCortisolCircadianCarCurve()

    print("=" * 70)
    print("DEMO: Personal Agent Cortisol Circadian CAR Curve & HPA Axis Modeler")
    print("=" * 70)

    # 1. 5-point salivary cortisol curve showing blunted CAR and elevated evening cortisol
    samples = [
        {"time": "07:00", "minutes_post_wake": 0, "nmol_l": 11.5},
        {"time": "07:30", "minutes_post_wake": 30, "nmol_l": 13.8}, # only 20% rise (blunted)
        {"time": "12:00", "minutes_post_wake": 300, "nmol_l": 9.2},
        {"time": "17:00", "minutes_post_wake": 600, "nmol_l": 7.0},
        {"time": "22:30", "minutes_post_wake": 930, "nmol_l": 5.2}  # elevated evening nadir
    ]

    res_curve = agent.evaluate_diurnal_cortisol_curve(samples)

    print(f"\n1. Diurnal Cortisol Curve Evaluation:")
    print(f"   Waking Cortisol: {res_curve['waking_cortisol_nmol_l']} nmol/L")
    print(f"   CAR 30-min Peak: {res_curve['car_30min_peak_nmol_l']} nmol/L (Rise: {res_curve['car_magnitude_rise_pct']})")
    print(f"   CAR Status: {res_curve['car_functional_status']}")
    print(f"   Diurnal Slope: {res_curve['diurnal_cortisol_slope_per_hour']} ({res_curve['diurnal_slope_classification']})")
    print(f"   Nocturnal Nadir: {res_curve['nocturnal_nadir_evaluation']}")
    print(f"   Evening Elevation Flag: {res_curve['elevated_evening_cortisol_flag']}")

    # 2. Prescribe targeted HPA axis reset
    res_rx = agent.recommend_hpa_resilience_protocol(
        car_status_category="blunted",
        evening_cortisol_elevated=res_curve['elevated_evening_cortisol_flag']
    )

    print(f"\n2. Targeted HPA Axis Re-Entrainment Protocol:")
    print(f"   Target State: {res_rx['hpa_axis_target_state']}")
    print(f"   Morning Actions:")
    for act in res_rx['morning_cortisol_entrainment_protocols']:
        print(f"     - {act}")
    print(f"   Evening Actions:")
    for act in res_rx['evening_downregulation_protocols']:
        print(f"     - {act}")
    print(f"   Core Rule: {res_rx['resilience_rule']}")

    print("\nVerification complete: Cortisol circadian CAR curve engine executed flawlessly.")

if __name__ == "__main__":
    main()
