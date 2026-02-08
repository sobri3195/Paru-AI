from __future__ import annotations

from emboli_ai.models import CTPAFindings, EHRSummary, RiskResult


class EmboliAIEngine:
    """Rule-based baseline untuk deteksi PE + stratifikasi risiko.

    Catatan:
    - Ini bukan model klinis tervalidasi.
    - Ditujukan sebagai baseline engineering yang bisa diganti model ML.
    """

    def assess(self, ctpa: CTPAFindings, ehr: EHRSummary) -> RiskResult:
        rationale: list[str] = []

        if not ctpa.filling_defect_present:
            return RiskResult(
                pe_classification="negative",
                risk_class="none",
                confidence=0.95,
                rationale=["Tidak ada filling defect pada CTPA."],
            )

        rationale.append("Filling defect terdeteksi pada CTPA.")

        hemodynamic_instability = ehr.systolic_bp < 90
        rv_strain = ctpa.rv_lv_ratio >= 1.0
        biomarker_positive = ehr.troponin_positive or ehr.bnp_positive
        hypoxemia = ehr.oxygen_saturation < 90

        if hemodynamic_instability:
            rationale.append("Hipotensi (SBP < 90) mendukung massive PE.")
            if ctpa.main_pulmonary_artery_involvement:
                rationale.append("Keterlibatan arteri pulmonalis utama meningkatkan risiko.")
            return RiskResult(
                pe_classification="positive",
                risk_class="massive",
                confidence=0.9,
                rationale=rationale,
            )

        if rv_strain:
            rationale.append(f"RV strain: rasio RV/LV {ctpa.rv_lv_ratio:.2f}.")
        if biomarker_positive:
            rationale.append("Biomarker jantung meningkat (troponin/BNP).")
        if hypoxemia:
            rationale.append(f"Hipoksemia: SpO2 {ehr.oxygen_saturation:.1f}%.")

        if rv_strain or biomarker_positive:
            return RiskResult(
                pe_classification="positive",
                risk_class="submassive",
                confidence=0.82,
                rationale=rationale,
            )

        rationale.append("Tidak ada instabilitas hemodinamik, RV strain, atau biomarker positif.")
        return RiskResult(
            pe_classification="positive",
            risk_class="low",
            confidence=0.78,
            rationale=rationale,
        )
