# -*- coding: utf-8 -*-
"""
Personal Agent Cortisol Circadian CAR Curve Client
Zero-dependency Cortisol Awakening Response (CAR) area-under-curve modeler, Diurnal
Cortisol Slope (DCS) flattener detector, and hypothalamic-pituitary-adrenal (HPA) axis stabilizer.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentCortisolCircadianCarCurve:
    """
    Quantifies circadian glucocorticoid dynamics, modeling the 30-minute Cortisol Awakening
    Response (CAR), diurnal slope decay rate, nocturnal nadir suppression, and HPA axis resilience.
    """

    def evaluate_diurnal_cortisol_curve(
        self,
        cortisol_samples_nmol_l: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Evaluates salivary free cortisol time-course:
        Expected format:
        [
          {'time': '07:00', 'minutes_post_wake': 0, 'nmol_l': 12.0},
          {'time': '07:30', 'minutes_post_wake': 30, 'nmol_l': 22.0},
          {'time': '12:00', 'minutes_post_wake': 300, 'nmol_l': 8.5},
          {'time': '17:00', 'minutes_post_wake': 600, 'nmol_l': 5.0},
          {'time': '22:30', 'minutes_post_wake': 930, 'nmol_l': 2.0}
        ]
        """
        if not cortisol_samples_nmol_l or len(cortisol_samples_nmol_l) < 2:
            return {"error": "At least 2 cortisol sample timepoints required (waking and post-waking or evening)."}

        # Sort by minutes post-wake
        samples = sorted(cortisol_samples_nmol_l, key=lambda x: float(x.get("minutes_post_wake", 0)))

        c_wake = float(samples[0].get("nmol_l", 12.0))
        c_30min = None
        c_night = float(samples[-1].get("nmol_l", 2.0))

        for s in samples:
            mins = float(s.get("minutes_post_wake", 0))
            if 20.0 <= mins <= 45.0:
                c_30min = float(s.get("nmol_l", 20.0))
                break

        # If 30-min CAR peak missing, estimate from second sample or baseline
        if c_30min is None and len(samples) > 1:
            c_30min = float(samples[1].get("nmol_l", c_wake * 1.5))

        # 1. Cortisol Awakening Response (CAR) Delta and Percentage Rise
        car_delta = round(c_30min - c_wake, 2)
        car_pct_rise = round((car_delta / max(1.0, c_wake)) * 100.0, 1)

        if car_pct_rise >= 50.0 and car_pct_rise <= 120.0:
            car_classification = "Robust Healthy CAR (Optimal prefrontal arousal & metabolic readiness)"
        elif car_pct_rise < 30.0:
            car_classification = "Blunted CAR (HPA Axis Hypo-Reactivity / Chronic Exhaustion / Burnout)"
        else:
            car_classification = "Hyper-Reactive CAR (Acute Stress / Morning Sympathetic Alarm)"

        # 2. Diurnal Cortisol Slope (DCS): Waking to Bedtime decline per hour
        total_hours = (float(samples[-1].get("minutes_post_wake", 960)) - float(samples[0].get("minutes_post_wake", 0))) / 60.0
        total_hours = max(8.0, total_hours)
        dcs_slope_per_hour = round((c_night - c_wake) / total_hours, 3)

        # Normal slope is steep negative (-0.6 to -1.2 nmol/L per hour)
        # Flat slope (> -0.4 nmol/L/h) correlates with chronic inflammation and systemic fatigue
        if dcs_slope_per_hour <= -0.6:
            slope_status = "Steep Healthy Diurnal Curve (Robust circadian amplitude)"
        elif dcs_slope_per_hour <= -0.35:
            slope_status = "Moderately Flattened Diurnal Slope (Incomplete daytime clearance)"
        else:
            slope_status = "Critically Flat Diurnal Curve (HPA Axis Exhaustion / Elevated Inflammatory Burden)"

        # 3. Nocturnal Nadir Status (Bedtime should be <= 3.5 nmol/L)
        if c_night <= 3.5:
            nadir_status = "Optimal Nocturnal Nadir (GABAergic sleep onset protected)"
            night_alert = False
        else:
            nadir_status = f"Elevated Nocturnal Cortisol ({c_night} nmol/L > 3.5 target): Sleep fragmentation risk"
            night_alert = True

        return {
            "waking_cortisol_nmol_l": c_wake,
            "car_30min_peak_nmol_l": c_30min,
            "bedtime_cortisol_nmol_l": c_night,
            "car_magnitude_rise_pct": f"{car_pct_rise}%",
            "car_functional_status": car_classification,
            "diurnal_cortisol_slope_per_hour": f"{dcs_slope_per_hour} nmol/L/hr",
            "diurnal_slope_classification": slope_status,
            "nocturnal_nadir_evaluation": nadir_status,
            "elevated_evening_cortisol_flag": night_alert
        }

    def recommend_hpa_resilience_protocol(
        self,
        car_status_category: str = "blunted",
        evening_cortisol_elevated: bool = False
    ) -> Dict[str, Any]:
        """
        Prescribes targeted chronobiological, nutritional, and breathwork interventions
        to re-entrain normal circadian HPA axis glucocorticoid pulsatility.
        """
        cat = str(car_status_category).lower()

        morning_actions = []
        evening_actions = []

        if "blunted" in cat or "hypo" in cat or "burnout" in cat:
            morning_actions.append("Direct outdoor sunlight immersion for 20 minutes within 15 minutes of waking.")
            morning_actions.append("Cold water facial plunge (stimulates sympathetic locus coeruleus norepinephrine).")
            morning_actions.append("Postpone intense high-glycolytic workouts until 15:00 - 17:00 when body temp is elevated.")
        elif "hyper" in cat or "alarm" in cat:
            morning_actions.append("Execute 5 minutes of cyclical physiological sighing (double inhale, slow prolonged exhale).")
            morning_actions.append("Delay caffeine intake 90 minutes post-wake to avoid compounding morning cortisol peak.")
            morning_actions.append("200mg L-Theanine with morning hydration to smooth glutamate-GABA balance.")
        else:
            morning_actions.append("Standard morning hydration with electrolytes and natural daylight.")

        if evening_cortisol_elevated:
            evening_actions.append("Enforce strict digital sunset: zero screens or 100% blue-blocking amber eyewear 2 hours before bed.")
            evening_actions.append("Magnesium L-Threonate (145mg) + Apigenin (50mg) 45 minutes prior to sleep.")
            evening_actions.append("Warm shower or bath to trigger peripheral vasodilation and core temperature drop.")
        else:
            evening_actions.append("Maintain dark, cool bedroom environment (18°C / 65°F).")

        return {
            "hpa_axis_target_state": "Restored Diurnal Glucocorticoid Rhythm",
            "morning_cortisol_entrainment_protocols": morning_actions,
            "evening_downregulation_protocols": evening_actions,
            "resilience_rule": "Cortisol is not toxic; it is the master circadian energizer when high in morning and low at night."
        }
