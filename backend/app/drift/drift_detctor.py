from .ks_test import KStest
from .psi import PSI

class DriftDetector:
    def __init__(self):
        self.ks = KStest()
        self.psi = PSI()

    def detect_feature_drift(self, reference, current):
        ks_result = self.ks.detect(reference, current)
        psi_result = self.psi.detect(reference, current)

        return{
            "ks_test" : ks_result,
            "psi" : psi_result,
            "drift" : ks_result["drift"] or psi_result["drift"]
        }

    def detect_dataset_drift(self, reference_df, current_df):
        report = {}

        for column in reference_df.columns:
            report[column] = self.detect_feature_drift(
                reference_df[column],
                current_df[column]

            )

        return report