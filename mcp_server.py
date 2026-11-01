# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Cortisol Circadian CAR Curve Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentCortisolCircadianCarCurve

mcp = FastMCP("PersonalAgentCortisolCircadianCarCurve")
client = PersonalAgentCortisolCircadianCarCurve()

@mcp.tool()
def evaluate_diurnal_cortisol_curve(
    cortisol_samples_nmol_l: list[dict]
) -> str:
    """Evaluates CAR 30-min peak, diurnal slope decay, and nocturnal nadir from salivary samples."""
    import json
    return json.dumps(client.evaluate_diurnal_cortisol_curve(cortisol_samples_nmol_l), indent=2)

@mcp.tool()
def recommend_hpa_resilience_protocol(
    car_status_category: str = "blunted",
    evening_cortisol_elevated: bool = False
) -> str:
    """Prescribes circadian light, breathwork, and nutritional protocols to restore HPA rhythm."""
    import json
    return json.dumps(client.recommend_hpa_resilience_protocol(car_status_category, evening_cortisol_elevated), indent=2)

if __name__ == "__main__":
    mcp.run()
