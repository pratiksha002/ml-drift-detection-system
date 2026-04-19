from scipy.stats import ks_2samp

class KStest:
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def detect(self, reference_data, current_data):
        stat, p_value = ks_2samp(reference_data, current_data)

        return{
            "method": "ks_test",
            "statistic": stat,
            "p_value": p_value,
            "drift": p_value < self.alpha
        }