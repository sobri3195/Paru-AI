from emboli_ai.engine import EmboliAIEngine
from emboli_ai.models import CTPAFindings, EHRSummary


def test_negative_when_no_filling_defect() -> None:
    result = EmboliAIEngine().assess(
        ctpa=CTPAFindings(filling_defect_present=False),
        ehr=EHRSummary(
            systolic_bp=120,
            heart_rate=90,
            oxygen_saturation=97,
            troponin_positive=False,
            bnp_positive=False,
        ),
    )
    assert result.pe_classification == "negative"
    assert result.risk_class == "none"


def test_massive_when_hypotension_present() -> None:
    result = EmboliAIEngine().assess(
        ctpa=CTPAFindings(
            filling_defect_present=True,
            main_pulmonary_artery_involvement=True,
            rv_lv_ratio=1.2,
        ),
        ehr=EHRSummary(
            systolic_bp=82,
            heart_rate=120,
            oxygen_saturation=86,
            troponin_positive=True,
            bnp_positive=True,
        ),
    )
    assert result.risk_class == "massive"


def test_submassive_when_rv_strain_or_biomarker() -> None:
    result = EmboliAIEngine().assess(
        ctpa=CTPAFindings(
            filling_defect_present=True,
            rv_lv_ratio=1.05,
        ),
        ehr=EHRSummary(
            systolic_bp=114,
            heart_rate=108,
            oxygen_saturation=92,
            troponin_positive=False,
            bnp_positive=False,
        ),
    )
    assert result.risk_class == "submassive"


def test_low_risk_when_stable_without_strain_marker() -> None:
    result = EmboliAIEngine().assess(
        ctpa=CTPAFindings(
            filling_defect_present=True,
            rv_lv_ratio=0.85,
        ),
        ehr=EHRSummary(
            systolic_bp=126,
            heart_rate=95,
            oxygen_saturation=95,
            troponin_positive=False,
            bnp_positive=False,
        ),
    )
    assert result.risk_class == "low"
