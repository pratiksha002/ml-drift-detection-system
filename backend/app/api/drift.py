from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd

from backend.app.drift.drift_detector import DriftDetector

router = APIRouter()

detector = DriftDetector()

from typing import List, Dict, Any

class DriftRequest(BaseModel):
    reference_data: List[Dict[str, Any]]
    current_data: List[Dict[str, Any]]


@router.post("/drift-report")
def get_drift_report(request: DriftRequest):
    reference_df = pd.DataFrame(request.reference_data)
    current_df = pd.DataFrame(request.current_data)

    report = detector.detect_dataset_drift(reference_df, current_df)

    return {
        "status": "success",
        "drift_report": report
    }