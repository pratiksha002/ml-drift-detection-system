import numpy as np

class PSI:
    def __init__(self, bins=10):
        self.bins = bins


    def calculate(self, expected, actual):
        breakpoints = np.linspace(0, 100, self.bins + 1)
        expected_bins = np.percentile(expected, breakpoints)

        psi = 0

        for i in range(len(expected_bins) - 1):
            e = ((expected >= expected_bins[i]) & (expected < expected_bins[i+1])).mean()
            a = ((actual >= expected_bins[i]) & (actual < expected_bins[i+1])).mean()

            e = max(e, 1e-6)
            a = max(a, 1e-6)

            psi += (e - a) * np.log(e/a)

        return psi
    
    def detect(self, expected, actual):
        psi_value = self.calculate(expected, actual)

        return{
            "method": "psi",
            "psi_value": round(float(psi_value), 5),
            "raw_psi_value": float(psi_value),
            "drift": bool(psi_value > 0.2)
        }