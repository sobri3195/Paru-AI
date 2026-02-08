from __future__ import annotations

import argparse
import json
from pathlib import Path

from emboli_ai.engine import EmboliAIEngine
from emboli_ai.models import CTPAFindings, EHRSummary


def main() -> None:
    parser = argparse.ArgumentParser(description="Emboli-AI CTPA prototype")
    parser.add_argument("--input", required=True, help="Path file JSON input")
    args = parser.parse_args()

    payload = json.loads(Path(args.input).read_text())

    ctpa = CTPAFindings(**payload["ctpa"])
    ehr = EHRSummary(**payload["ehr"])

    result = EmboliAIEngine().assess(ctpa=ctpa, ehr=ehr)
    print(json.dumps(result.__dict__, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
