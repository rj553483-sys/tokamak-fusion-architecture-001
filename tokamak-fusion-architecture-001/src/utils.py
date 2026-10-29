"""
Utility Functions for Tokamak System Scaling and Structural Mechanics.
Manuscript ID: Fusion-Arch-001 (Paper VII)
"""

import numpy as np


def calculate_ip_scaling(R0: float, a: float, B0: float, kappa: float, q95: float) -> float:
    """
    Calculates plasma current Ip (MA) using tokamak MHD safety factor scaling:
    Ip = (5 * a^2 * B0 / (R0 * q95)) * ((1 + kappa^2) / 2)
    """
    epsilon = a / R0
    ip_ma = (5.0 * (a ** 2) * B0 / (R0 * q95)) * ((1.0 + kappa ** 2) / 2.0)
    return ip_ma


def evaluate_tsai_wu_structural_reserve(
    sigma_1: float,
    sigma_2: float,
    tau_12: float,
    F1: float = 1.2e-4,
    F2: float = 1.2e-4,
    F11: float = 1.5e-6,
    F22: float = 1.5e-6,
    F66: float = 4.0e-6,
    F12: float = -0.75e-6
) -> dict:
    """
    Evaluates the 3D anisotropic Tsai-Wu structural failure criterion:
    FI = F1*sigma1 + F2*sigma2 + F11*sigma1^2 + F22*sigma2^2 + F66*tau12^2 + 2*F12*sigma1*sigma2 <= 1.0
    """
    fi = (
        F1 * sigma_1
        + F2 * sigma_2
        + F11 * (sigma_1 ** 2)
        + F22 * (sigma_2 ** 2)
        + F66 * (tau_12 ** 2)
        + 2.0 * F12 * sigma_1 * sigma_2
    )
    fos = 1.0 / np.sqrt(fi) if fi > 0 else 999.0
    srr = (1.0 - fi) / fi if fi > 0 else 999.0
    return {
        "failure_index": float(fi),
        "factor_of_safety": float(fos),
        "structural_reserve_ratio": float(srr),
        "is_safe": bool(fi <= 1.0)
    }


def calculate_rebco_magnetic_energy_density(B0: float, mu0: float = 4.0 * np.pi * 1e-7) -> float:
    """
    Calculates TF magnet loop magnetic energy density e_m = B0^2 / (2 * mu0) in MJ/m^3.
    """
    e_joules = (B0 ** 2) / (2.0 * mu0)
    return e_joules / 1.0e6
