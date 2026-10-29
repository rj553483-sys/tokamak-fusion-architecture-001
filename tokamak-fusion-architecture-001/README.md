# Tokamak Fusion Architecture 001: Compact High-Field Tokamak Fusion Reactor

## Overview & System Architecture

This repository contains the complete, production-ready code, multi-physics design models, verification data, and manuscript deliverables for **Paper VII**:
> **"System Architecture and Multi-Physics Design of a Compact High-Field Tokamak Fusion Reactor"**  
> *Manuscript ID:* **Fusion-Arch-001**  
> *Target Journal:* **Fusion Engineering and Design** (Elsevier, Traditional No-Fee Subscription Publishing Model)  
> *Author:* **Jacob (Jake) James Rasmussen** (ORCID: 0009-0009-7084-6523)

---

## Key Reactor Engineering Parameters

- **Major Radius (R0)**: 3.30 m
- **Minor Radius (a)**: 1.10 m (Aspect ratio A = 3.0)
- **Toroidal Field (B0)**: 12.20 T (On-axis magnetic field strength B0 >= 10 T)
- **Plasma Current (Ip)**: 8.54 MA (MHD safety factor scaling q95 = 3.20, Ip >= 8 MA)
- **REBCO Energy Density (em)**: 59.18 MJ/m^3 (High-field HTS TF coil magnetic energy density)
- **Divertor Peak Heat Flux (q''_peak)**: 15.00 MW/m^2 (Handled via CPS vapor shielding cushion)
- **CPS Dryout Limit (q''_dryout)**: 22.50 MW/m^2 (Capillary porous system Young-Laplace dryout threshold)
- **Tritium Breeding Ratio (TBR)**: 1.18 (Dual-Coolant Lead-Lithium DCLL blanket)
- **Hartmann Number (Ha)**: 10,000 (High Ha MHD Shercliff side-wall jet profile)
- **Tsai-Wu Yield Index (FI)**: 0.244 (3D anisotropic structural safety margin FI <= 1.0)
- **Factor of Safety (FOS)**: 1.61 (Cryogenic Inconel 718 keyways under VDE halo shear)

---

## Directory Structure

```
tokamak-fusion-architecture-001/
├── LICENSE (MIT License)
├── README.md (Comprehensive landing page & documentation)
├── CITATION.cff (Academic CFF format with ORCID)
├── requirements.txt (Python dependency specification)
├── docs/
│   ├── Main_Manuscript.pdf (Full paper text for Fusion-Arch-001)
│   ├── Cover_Letter.pdf (Official cover letter selecting subscription model)
│   ├── Highlights.pdf (Core submission highlights, <= 85 chars/bullet)
│   └── Supplementary_Information.pdf (ESI power balance & geometry specs)
├── src/
│   ├── __init__.py
│   ├── reactor_system_model.py (Core power balance & magnetic field solver)
│   └── utils.py (Ip scaling & Tsai-Wu structural evaluation metrics)
├── data/
│   ├── reactor_design_point.csv (Key engineering dimensions & loads)
│   └── system_verification.json (Global convergence status & residuals < 0.015%)
├── figures/
│   ├── figure1_300dpi.png through figure4_300dpi.png (High-res 300 DPI panels)
│   └── figure1_vector.svg through figure4_vector.svg (Scalable vector versions)
└── .github/
    └── workflows/
        └── python-test.yml (Automated CI/CD verification runner)
```

---

## Quickstart & Execution Guide

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute System Architecture Verification Solver**:
   ```bash
   python src/reactor_system_model.py
   ```

---

## Citation & Publication Metadata

If using this reactor design point or code suite, please cite:
```bibtex
@article{Rasmussen2026_FusionArch001,
  author    = {Rasmussen, Jacob James},
  title     = {System Architecture and Multi-Physics Design of a Compact High-Field Tokamak Fusion Reactor},
  journal   = {Fusion Engineering and Design},
  year      = {2026},
  note      = {Manuscript ID: Fusion-Arch-001},
  orcid     = {0009-0009-7084-6523}
}
```
