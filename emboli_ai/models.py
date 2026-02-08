from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class CTPAFindings:
    filling_defect_present: bool
    main_pulmonary_artery_involvement: bool = False
    rv_lv_ratio: float = 0.9
    clot_burden_score: float = 0.0


@dataclass
class EHRSummary:
    systolic_bp: int
    heart_rate: int
    oxygen_saturation: float
    troponin_positive: bool
    bnp_positive: bool


@dataclass
class RiskResult:
    pe_classification: str
    risk_class: str
    confidence: float
    rationale: List[str] = field(default_factory=list)
