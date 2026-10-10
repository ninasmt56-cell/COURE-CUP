import streamlit as st

st.title("CUORE AI Recommendation System")
st.write("Welcome to CUORE Modular Porridge Recommender!")

sbp = st.number_input("Enter Blood Pressure (Systolic mmHg):", value=135)
diet = st.selectbox("Primary Dietary Pattern:", ["High Sodium / Salty", "High Fat", "Low Fibre"])

if st.button("Analyze Recommendation"):
    if sbp >= 130 or diet == "High Sodium / Salty":
        st.success("Recommended Module: S-CUP (Sodium Conscious)")
    elif diet == "High Fat":
        st.info("Recommended Module: L-CUP (Lipid Oriented)")
    else:
        st.success("Recommended Module: M-CUP (Metabolic Oriented)")