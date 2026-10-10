import streamlit as st

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="CUORE AI Web Interface Mockup",
    page_icon="🥣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Injeksi CSS & HTML Kustom untuk Animasi, Gradient, dan Kartu Pastel
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Reset Background Utama ke Pastel Gradient Soft */
    .stApp {
        background: linear-gradient(135deg, #FFF5F2 0%, #FFFBF5 40%, #F0FDF4 100%) !important;
        font-family: 'Poppins', sans-serif;
        color: #334155;
    }

    /* Keyframe Animasi Floating & Pulsing */
    @keyframes floatSlow {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-12px) rotate(1.5deg); }
    }

    @keyframes pulseGlowPink {
        0%, 100% { box-shadow: 0 10px 25px rgba(244, 114, 182, 0.3); }
        50% { box-shadow: 0 15px 35px rgba(244, 114, 182, 0.6); }
    }

    @keyframes pulseGlowGreen {
        0%, 100% { box-shadow: 0 10px 25px rgba(52, 211, 153, 0.3); }
        50% { box-shadow: 0 15px 35px rgba(52, 211, 153, 0.6); }
    }

    @keyframes pulseGlowPurple {
        0%, 100% { box-shadow: 0 10px 25px rgba(167, 139, 250, 0.3); }
        50% { box-shadow: 0 15px 35px rgba(167, 139, 250, 0.6); }
    }

    @keyframes spinRing {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* Kartu UI Pastel */
    .glass-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 24px;
        border: 1px solid rgba(255, 255, 255, 0.6);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
        margin-bottom: 20px;
    }

    /* Cup Animated Modules */
    .cup-container {
        display: flex;
        justify-content: space-around;
        align-items: flex-end;
        gap: 15px;
        margin-top: 20px;
    }

    .cup-card {
        border-radius: 24px;
        padding: 20px 15px;
        text-align: center;
        flex: 1;
        transition: all 0.4s ease;
        animation: floatSlow 4s ease-in-out infinite;
    }

    .cup-pink {
        background: linear-gradient(180deg, #FFE4E6 0%, #FECDD3 100%);
        border: 2px solid #FB7185;
        animation-delay: 0s;
        animation: pulseGlowPink 3s infinite, floatSlow 4s ease-in-out infinite;
    }

    .cup-green {
        background: linear-gradient(180deg, #D1FAE5 0%, #A7F3D0 100%);
        border: 2px solid #34D399;
        animation-delay: 0.5s;
        animation: pulseGlowGreen 3s infinite 0.5s, floatSlow 4.2s ease-in-out infinite 0.5s;
    }

    .cup-purple {
        background: linear-gradient(180deg, #EDE9FE 0%, #DDD6FE 100%);
        border: 2px solid #A78BFA;
        animation-delay: 1s;
        animation: pulseGlowPurple 3s infinite 1s, floatSlow 4.5s ease-in-out infinite 1s;
    }

    /* Ring AI Optimizing Visualizer */
    .ai-ring-box {
        position: relative;
        width: 180px;
        height: 180px;
        margin: 0 auto 15px auto;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .ai-ring {
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 8px solid transparent;
        border-top-color: #F472B6;
        border-right-color: #34D399;
        border-bottom-color: #A78BFA;
        border-left-color: #FBBF24;
        animation: spinRing 6s linear infinite;
    }

    .ai-ring-inner {
        width: 80%;
        height: 80%;
        background: white;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: inset 0 2px 10px rgba(0,0,0,0.05);
        z-index: 2;
    }
</style>
""", unsafe_allow_html=True)

# 1. Header & Logo Terracotta CUORE
st.markdown("""
<div style="display: flex; align-items: center; gap: 15px; margin-bottom: 25px;">
    <div style="background-color: #D1A880; width: 60px; height: 60px; border-radius: 50%; padding: 2px; box-shadow: 0 4px 10px rgba(192,86,56,0.2);">
        <div style="border: 2px dashed #B88A5F; width: 100%; height: 100%; border-radius: 50%; background-color: #C05638; display: flex; flex-direction: column; align-items: center; justify-content: center; color: white;">
            <span style="font-family: 'Fredoka', sans-serif; font-size: 11px; font-weight: bold; letter-spacing: 1px;">CUORE</span>
            <span style="font-size: 8px;">🌾🥣🌾</span>
        </div>
    </div>
    <div>
        <h1 style="font-family: 'Fredoka', sans-serif; color: #C05638; margin: 0; font-size: 2rem; font-weight: 700;">CUORE</h1>
        <p style="color: #64748B; margin: 0; font-size: 0.85rem; font-style: italic;">Local comfort, thoughtfully engineered</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Layout Grid 2 Kolom Utama (Kiri: Profile & AI Engine, Kanan: Modules & Nutrition)
col_left, col_right = st.columns([5, 7])

with col_left:
    # COMPONENT 1: Health & Preference Profile
    st.markdown("""
    <div class="glass-card">
        <h3 style="font-family: 'Fredoka', sans-serif; color: #1E293B; margin-top: 0;">Health & Preference Profile</h3>
        <div style="display: flex; align-items: center; gap: 15px; margin-top: 15px; background: white; padding: 15px; border-radius: 18px; border: 1px solid #E2E8F0;">
            <div style="font-size: 35px;">👩‍⚕️</div>
            <div>
                <h4 style="margin: 0; color: #0F172A; font-size: 1rem;">Kathryn</h4>
                <p style="margin: 2px 0 0 0; color: #64748B; font-size: 0.8rem;"><b>Blood Pressure:</b> 138/88 mmHg (Voluntary Input)</p>
                <p style="margin: 2px 0 0 0; color: #64748B; font-size: 0.8rem;"><b>Dietary Preference:</b> Low Salt, Plant-Based</p>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 8px; margin-top: 15px; color: #059669; font-weight: 600; font-size: 0.85rem;">
            <span>D Verified Data Consent (PDP Law Compliance)</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # AI Optimizing Ring Visualizer
    st.markdown("""
    <div class="glass-card" style="text-align: center;">
        <div class="ai-ring-box">
            <div class="ai-ring"></div>
            <div class="ai-ring-inner">
                <span style="font-size: 20px;">🌾</span>
                <span style="font-family: 'Fredoka', sans-serif; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Optimizing...</span>
                <span style="font-size: 0.65rem; color: #64748B;">(Conceptual Prototype)</span>
            </div>
        </div>
        <h4 style="font-family: 'Fredoka', sans-serif; color: #C05638; margin: 5px 0;">AI Recommendation:</h4>
        <p style="color: #475569; font-size: 0.85rem; margin: 0;">Personalized Formulation Matched</p>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    # COMPONENT 2: Personalised CUORE Modules (Pink, Green, Purple Floating Cups)
    st.markdown("""
    <div class="glass-card">
        <h3 style="font-family: 'Fredoka', sans-serif; color: #1E293B; margin-top: 0;">Personalised CUORE Modules</h3>
        <p style="color: #64748B; font-size: 0.8rem; margin-bottom: 10px;">CUORE Modul L/M/S (Pink, Green, Purple cups with gentle floating & pulsing effect).</p>
        
        <div class="cup-container">
            <!-- S-CUP (Pink) -->
            <div class="cup-card cup-pink">
                <span style="font-size: 28px;">💖</span>
                <h4 style="font-family: 'Fredoka', sans-serif; color: #9D174D; margin: 5px 0 2px 0;">Sodium-Conscious</h4>
                <span style="font-size: 0.7rem; font-weight: 700; color: #BE123C; background: rgba(255,255,255,0.7); padding: 2px 8px; border-radius: 10px;">S-CUP (Pink)</span>
            </div>
            
            <!-- M-CUP (Green) -->
            <div class="cup-card cup-green">
                <span style="font-size: 28px;">💚</span>
                <h4 style="font-family: 'Fredoka', sans-serif; color: #065F46; margin: 5px 0 2px 0;">Resistant Starch</h4>
                <span style="font-size: 0.7rem; font-weight: 700; color: #047857; background: rgba(255,255,255,0.7); padding: 2px 8px; border-radius: 10px;">M-CUP (Green)</span>
            </div>

            <!-- L-CUP (Purple) -->
            <div class="cup-card cup-purple">
                <span style="font-size: 28px;">💜</span>
                <h4 style="font-family: 'Fredoka', sans-serif; color: #5B21B6; margin: 5px 0 2px 0;">Lipid-Priority</h4>
                <span style="font-size: 0.7rem; font-weight: 700; color: #6D28D9; background: rgba(255,255,255,0.7); padding: 2px 8px; border-radius: 10px;">L-CUP (Purple)</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # COMPONENT 3: Nutrition & Ingredient Information
    st.markdown("""
    <div class="glass-card">
        <h3 style="font-family: 'Fredoka', sans-serif; color: #1E293B; margin-top: 0;">Nutrition & Ingredient Information</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 15px;">
            <div style="background: white; padding: 12px; border-radius: 14px; border: 1px solid #E2E8F0;">
                <span style="color: #64748B; font-size: 0.75rem; font-weight: 600;">Sorghum:</span>
                <h4 style="margin: 2px 0 0 0; color: #0F172A; font-size: 1.1rem; font-weight: 700;">15g</h4>
            </div>
            <div style="background: white; padding: 12px; border-radius: 14px; border: 1px solid #E2E8F0;">
                <span style="color: #64748B; font-size: 0.75rem; font-weight: 600;">Tempeh:</span>
                <h4 style="margin: 2px 0 0 0; color: #0F172A; font-size: 1.1rem; font-weight: 700;">5g</h4>
            </div>
            <div style="background: #FEF2F2; padding: 12px; border-radius: 14px; border: 1px solid #FCA5A5;">
                <span style="color: #991B1B; font-size: 0.75rem; font-weight: 700;">Allergen Alert:</span>
                <h4 style="margin: 2px 0 0 0; color: #991B1B; font-size: 0.95rem; font-weight: 700;">Soy</h4>
            </div>
            <div style="background: white; padding: 12px; border-radius: 14px; border: 1px solid #E2E8F0;">
                <span style="color: #64748B; font-size: 0.75rem; font-weight: 600;">Serving Instructions:</span>
                <p style="margin: 2px 0 0 0; color: #334155; font-size: 0.7rem; leading-height: 1.2;">Pour hot water, stir well, and serve warm in cup.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
