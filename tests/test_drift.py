import pandas as pd
import numpy as np
from backend.app.drift.drift_detector import DriftDetector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

np.random.seed(42)

reference = pd.DataFrame({
    "age" : np.random.normal(30, 5, 1000),
    "income" : np.random.normal(50000, 10000, 1000)
})

current = pd.DataFrame({
    "age": np.random.normal(40, 5, 1000),
    "income": np.random.normal(50000, 10000, 1000)
})

detector = DriftDetector()
report = detector.detect_dataset_drift(reference, current)

print(report)