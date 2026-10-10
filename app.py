import streamlit as st

# 1. Konfigurasi Halaman & Tema
st.set_page_config(
    page_title="CUORE - AI Web Dashboard Mockup",
    page_icon="🥣",
    layout="wide"
)

# Custom Styling CSS untuk tampilan UI Modern
st.markdown("""
<style>
    .main-title {
        color: #C05638;
        font-family: 'Fredoka', sans-serif;
        font-weight: 700;
        font-size: 2.2rem;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #64748B;
        font-size: 0.9rem;
        margin-bottom: 20px;
    }
    .badge-prototype {
        background-color: #FEF3C7;
        color: #92400E;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid #FCD34D;
    }
    .card-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 2. Header Dashboard
st.markdown('<span class="badge-prototype">PROPOSED INTERFACE / CONCEPTUAL PROTOTYPE</span>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">CUORE AI Web Interface Mockup</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Integrated Non-Diagnostic Recommendation System & Nutrition Transparency</p>', unsafe_allow_html=True)

st.info("⚠️ **Note for Reviewers:** Non-diagnostic decision-support interface for research & demonstration purposes (IYC 2026).")

# 3. Baris Atas: Split 2 Kolom (1. User Health Profile & 2. AI Recommendation)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 👤 1. Health & Preference Profile")
    with st.container():
        user_name = st.text_input("User Name", "Kathryn")
        col_age, col_bp = st.columns(2)
        with col_age:
            age = st.number_input("Age (Years)", value=45)
        with col_bp:
            sbp = st.number_input("Systolic BP (mmHg)", value=138)
        
        diet = st.selectbox(
            "Primary Dietary Pattern Focus (FFQ):",
            ["High Sodium / Salty Foods", "High Fat / Fried Foods", "Low Fibre / Sugary Foods"]
        )
        
        consent = st.checkbox("Verified Voluntary Data Consent (PDP Law Compliance)", value=True)
        safety = st.checkbox("Safety Exclusion Verified (No pregnancy/severe renal/soy allergy)", value=True)

with col2:
    st.markdown("### 🤖 2. AI-Based CUORE Recommendation")
    with st.container():
        st.write("**Module Classifier Output Matching:**")
        
        # Logika Penentuan Modul
        if sbp >= 130 or diet == "High Sodium / Salty Foods":
            rec_module = "S-CUP (Sodium-Conscious Flavour Architecture)"
            mod_color = "💖 Pink Packaging Variant"
            rationale = "Target priority identified for Sodium-Conscious Flavour Architecture based on reported systolic blood pressure and salty food frequency. Utilizes oyster mushroom & allium umami compounds."
            badge_type = "error"
        elif diet == "High Fat / Fried Foods":
            rec_module = "L-CUP (Viscous Soluble Fibre & Bioactives)"
            mod_color = "💜 Purple Packaging Variant"
            rationale = "Target priority identified for Viscous Soluble Fibre & Lipid Priority. Formulated with Porang glucomannan (6g) & basil seeds (4g) for lipid-binding mechanism."
            badge_type = "secondary"
        else:
            rec_module = "M-CUP (Resistant Starch & Protein Emphasis)"
            mod_color = "💚 Green Packaging Variant"
            rationale = "Target priority identified for Resistant Starch & Metabolic Energy Stability. Enhanced with unripe banana flour (7g) and fermented tempeh protein."
            badge_type = "success"
        
        st.success(f"**Matched Serving Composition:**\n- **Base Portion:** Universal Base (35g)\n- **Selected Module:** {rec_module} (20g)")
        st.markdown(f"**Packaging Color Code:** `{mod_color}`")
        st.caption(f"**AI Classifier Rationale:** {rationale}")

st.divider()

# 4. Baris Bawah: 3. Nutrition & Ingredient Transparency
st.markdown("### 🌿 3. Nutrition, Composition & Safety Transparency")

col_nut, col_ing, col_prep = st.columns(3)

with col_nut:
    st.markdown("**Nutritional Profile (per 55g serving):**")
    st.metric(label="Estimated Energy", value="≈ 203 kcal")
    st.metric(label="Protein Content", value="8.1 g")
    st.metric(label="Dietary Fibre", value="5.5 g")
    st.metric(label="Intrinsic Sodium", value="17 mg", delta="<1% WHO Daily Limit")

with col_ing:
    st.markdown("**Formulation Breakdown:**")
    st.write("**Universal Base (35g):** Sorghum (15g), Red Rice (8g), Tempeh Flour (5g), Mung Bean (4g), Oyster Mushroom (1g), Garlic (1g), Shallot (1g).")
    st.write("**Selected Module (20g):** Specific botanical actives tailored by AI classification.")

with col_prep:
    st.markdown("**Safety & Preparation:**")
    st.warning("⚠️ **Allergen Alert:** Contains Soy (Fermented Tempeh Flour).")
    st.info("☕ **Preparation:** Empty Universal Base and Module sachets into the cup, add 150ml hot water, stir well, and serve.")
