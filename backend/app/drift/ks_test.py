from scipy.stats import ks_2samp

class KStest:
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def detect(self, reference_data, current_data):
        stat, p_value = ks_2samp(reference_data, current_data)

        return{
            "method": "ks_test",
            "statistic": round(float(stat), 5),
            "p_value": round(float(p_value), 5),
            "raw_p_value": float(p_value),
            "drift": bool(p_value < self.alpha)
        }