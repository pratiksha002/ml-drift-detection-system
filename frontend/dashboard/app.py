import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("ML Drift Monitoring Dashboard")
st.write("Uplod reference and current data to detect drift")

ref_file = st.file_uploader("Upload Reference data (CSV)", type=["csv"])
curr_file = st.file_uploader("Upload Current data (CSV)", type=["csv"])

if ref_file and curr_file:
    ref_df = pd.read_csv(ref_file)
    curr_df = pd.read_csv(curr_file)

    ref_df = ref_df.apply(pd.to_numeric, errors='coerce')
    curr_df = curr_df.apply(pd.to_numeric, errors='coerce')

    st.subheader("Reference Data")
    st.write(ref_df.head())

    st.subheader("Current Data")
    st.write(curr_df.head())

    if st.button("Detect Drift"):
        payload = {
            "reference_data": ref_df.to_dict(orient="records"),
            "current_data": curr_df.to_dict(orient="records")
        }

        response = requests.post(
            "http://127.0.0.1:8000/drift-report",
            json=payload
        )

        result = response.json()

        st.subheader("Drift Report")
        st.json(result)

        st.subheader("Drift Alerts")

        for feature, data in result["drift_report"].items():
            if data["drift"]:
                st.error(f"{feature} has drift!")

            else:
                st.success(f"{feature} is stable")

            st.subheader("Feature Drift Ranking")

            psi_scores = {
                feature: data["psi"]["psi_value"]
                for feature, data in result["drift_report"].items()
            }

            sorted_features = sorted(psi_scores.items(), key=lambda x: x[1], reverse=True)

            for feature, score in sorted_features:
                st.write(f"{feature}: {score}")


            st.subheader("Feature Distribution Comparison")

            for feature in ref_df.columns:
                fig, ax = plt.subplots()

                ax.hist(ref_df[feature].dropna(), bins=30, alpha=0.5, label="Reference")
                ax.hist(curr_df[feature].dropna(), bins=30, alpha=0.5, label="Current")

                ax.set_title(f"{feature} Distribution Comparison")
                ax.legend()

                st.pyplot(fig)