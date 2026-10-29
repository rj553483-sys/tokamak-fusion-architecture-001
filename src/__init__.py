"""
Unified High-Field Tokamak Fusion Architecture Simulation Suite
Manuscript ID: Fusion-Arch-001 (Paper VII)
Target Journal: Fusion Engineering and Design
Author: Jacob James Rasmussen (ORCID: 0009-0009-7084-6523)
"""

from .reactor_system_model import TokamakSystemModel, solve_reactor_power_balance
from .utils import calculate_ip_scaling, evaluate_tsai_wu_structural_reserve

__version__ = "1.0.0"
__all__ = [
    "TokamakSystemModel",
    "solve_reactor_power_balance",
    "calculate_ip_scaling",
    "evaluate_tsai_wu_structural_reserve",
]
