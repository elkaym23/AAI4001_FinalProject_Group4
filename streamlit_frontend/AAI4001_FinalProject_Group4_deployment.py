import streamlit as st
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Crop Yield Prediction Dashboard",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* -------------------------------------------------------
   FIX TOP WHITE STRIP + MAKE ALL BACKGROUNDS CONSISTENT
--------------------------------------------------------*/
html, body, .stApp, .stAppViewContainer,
.block-container, .main,
header[data-testid="stHeader"] {
    background-color: #f5f5f0 !important;
}

/* Global Styles (your original CSS continues below) */
.main {
    background-color: #f5f5f0;
    padding: 2rem;
}
    
    /* Header Styles */
    h1 {
        color: #3d4f3d;
        font-weight: 600;
        font-size: 2.5rem;
    }
    
    h2, h3 {
        color: #5a6d5a;
        font-weight: 500;
    }
    
    /* Subtitle */
    .subtitle {
        color: #7a8a7a;
        font-size: 1.1rem;
        margin-top: -1rem;
        margin-bottom: 2rem;
    }
    
    /* Tab Navigation */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background-color: transparent;
        border-bottom: 2px solid #d4dbd4;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.75rem 1.5rem;
        background-color: transparent;
        border-radius: 8px 8px 0 0;
        font-weight: 500;
        color: #7a8a7a;
        border: none;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #7a9b7a;
        color: white;
    }
    
    /* Cards - White with subtle shadow */
    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border-left: 4px solid #7a9b7a;
        margin: 1rem 0;
            align-items: center;
            text-align: center;
    }
    
    .metric-card h2 {
        color: #3d4f3d;
        margin-bottom: 0.5rem;
    }
    
    .metric-card h1 {
        color: #7a9b7a;
        font-size: 3rem;
        margin: 0.5rem 0;
    }
    
    /* Info boxes with sage accent */
    .info-box {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #7a9b7a;
        margin: 1rem 0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }
    
    .info-box h3, .info-box h4 {
        color: #3d4f3d;
        margin-bottom: 0.75rem;
    }
    
    /* Insight cards with lighter sage */
    .insight-card {
        background-color: #f0f4f0;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #9bb89b;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .insight-card h4 {
        color: #3d4f3d;
        margin-bottom: 0.5rem;
    }
    
    /* Warning boxes with warm accent */
    .warning-box {
        background-color: #fef9f5;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #c9a87c;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .warning-box h4 {
        color: #8b6f47;
        margin-bottom: 0.5rem;
    }
    
    /* Challenge Cards - Icon cards for introduction */
    .challenge-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        text-align: center;
        margin: 1rem 0;
        transition: transform 0.2s;
    }
    
    .challenge-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }
    
    .challenge-card h4 {
        color: #3d4f3d;
        margin: 1rem 0 0.5rem 0;
    }
    
    .challenge-card p {
        color: #7a8a7a;
        font-size: 0.9rem;
    }
    
    /* Jamaica Focus Badge */
    .badge {
        display: inline-block;
        background-color: #c9a87c;
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    /* Objective Cards */
    .objective-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        margin: 1rem 0;
        display: flex;
        gap: 1.5rem;
        align-items: start;
    }
    
    .objective-number {
        background: #7a9b7a;
        color: white;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: bold;
        flex-shrink: 0;
    }
    
    /* Stats Cards */
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        text-align: center;
    }
    
    .stat-card h1 {
        color: #7a9b7a;
        font-size: 2.5rem;
        margin: 0.5rem 0;
    }
    
    .stat-card p {
        color: #7a8a7a;
        margin: 0;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #7a9b7a;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    
    .stButton>button:hover {
        background-color: #6a8b6a;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #f5f5f0;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #7a9b7a;
        font-size: 1.8rem;
    }
    
    /* Dataframe */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }
    
    /* Select boxes and inputs */
    .stSelectbox, .stNumberInput, .stSlider {
        margin-bottom: 1rem;
    }
    
    /* Remove default streamlit styling */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

/* SIDEBAR WRAPPER */
section[data-testid="stSidebar"] {
    background-color: #f5f5f0 !important;
    padding: 1.5rem !important;
}

/* SIDEBAR TITLE */
.sidebar-title {
    font-size: 1.6rem;
    font-weight: 600;
    color: #3d4f3d;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

/* Foldable card sections */
.sidebar-card {
    background: white;
    padding: 1.5rem;
    border-radius: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border: 1px solid #e2e8e2;
    margin-bottom: 1.5rem;
}

.sidebar-card h3 {
    color: #3d4f3d;
    font-size: 1.2rem;
    margin-bottom: 0.75rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.sidebar-card label {
    color: #5a6d5a !important;
    font-weight: 500 !important;
}

/* Drop-downs, sliders, switches */
.sidebar-card .stSelectbox,
.sidebar-card .stSlider,
.sidebar-card .stNumberInput {
    margin-bottom: 1rem !important;
}

/* Train Model Button */
.sidebar-button > button {
    width: 100%;
    background-color: #7a9b7a !important;
    color: white !important;
    padding: 0.75rem;
    font-weight: 600;
    border-radius: 12px;
}

.sidebar-button > button:hover {
    background-color: #6a8b6a !important;
}

/* Fix for toggle switch */
.st-af {
    accent-color: #7a9b7a !important;
}


    
    </style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# THEME ENGINE (LIGHT / DARK MODE)
# ---------------------------------------------------------
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "light"

st.markdown("""
<script>
const observer = new MutationObserver(() => {
    const isDark = document.body.classList.contains('dark');
    window.parent.postMessage({themeMode: isDark ? "dark" : "light"}, "*");
});
observer.observe(document.body, {attributes: true});
</script>
""", unsafe_allow_html=True)

msg = msg = st.query_params.get("themeMode")
if msg:
    st.session_state.theme_mode = msg[0]

LIGHT = {
    "primary": "#7a9b7a",
    "muted": "#7a8a7a",
    "card": "#ffffff",
}
DARK = {
    "primary": "#4e634e",
    "muted": "#cdd5cd",
    "card": "#2b302b",
}
THEME = DARK if st.session_state.theme_mode == "dark" else LIGHT

# ---------------------------------------------------------
# MAIN HEADER
# ---------------------------------------------------------
st.markdown(f"""
<div style="display:flex;align-items:center;margin-bottom:1rem;">
    <span style="font-size:3rem;margin-right:1rem;">🌱</span>
    <div>
        <h1>Crop Yield Prediction Dashboard</h1>
        <p class="subtitle">Machine Learning insights for climate & agricultural planning</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# TABS 
# ---------------------------------------------------------
tab1, tab2 = st.tabs([
    
    "🎯 Live Yield Model",
    "📖 About Model",
    
])


# ---------------------------------------------------------
# TAB 1 — LIVE MODEL (FASTAPI PREDICTION)
# ---------------------------------------------------------
with tab1:

    st.header("🎯 Interactive Crop Yield Prediction (Live Model)")

    # ---------------- SIDEBAR -----------------
    with st.sidebar:

        # -----------------------
        # TITLE
        # -----------------------
        st.markdown('<div class="sidebar-title">🌾 Model Inputs</div>', unsafe_allow_html=True)

        # -----------------------
        # CROP & YEAR
        # -----------------------
        crop = st.selectbox(
            "Crop Type",
            [
                "Maize", "Potatoes", "Rice, paddy", "Wheat", "Sorghum",
                "Soybeans", "Sweet potatoes", "Plantains and others", "Yams"
            ]
        )

        year = st.number_input(
            "Year",
            min_value=1990,
            max_value=2050,
            value=2025,
            step=1
        )

        # -----------------------
        # CLIMATE VARIABLES
        # -----------------------
        rainfall = st.number_input(
            "Average Rainfall (mm/year)",
            min_value=0,
            max_value=4000,
            value=1200,
            step=10
        )


        temp = st.number_input(
            "Average Temperature (°C)",
            min_value=0.0,
            max_value=40.0,
            value=20.0,
            step=0.1
        )


        # -----------------------
        # AGRICULTURAL INPUTS
        # -----------------------
        pesticides = st.number_input(
            "Pesticides Used (tonnes)",
            min_value=0.0,
            max_value=400000.0,
            value=500.0,
            step=1.0
        )


        # -----------------------
        # BUTTON
        # -----------------------
        run_prediction = st.button("🚀 Predict Yield", use_container_width=True)


    # ---------------- MODEL REQUEST -----------------
    if run_prediction:
        payload = {
            "Item": crop,
            "Year": int(year),
            "average_rain_fall_mm_per_year": float(rainfall),
            "avg_temp": float(temp),
            "pesticides_tonnes": float(pesticides)
        }

        try:
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)

            if response.status_code == 200:
                prediction = response.json()["predicted_yield_hg_per_ha"]

                st.markdown(f"""
                    <div class="metric-card">
                        <h2>🌾 Predicted Crop Yield</h2>
                        <h1>{prediction:,.2f} hg/ha</h1>
                        <h1>{prediction * 0.04047:,.2f} kg/acre</h1>
                        <h1>{prediction * 0.08921:,.2f} lb/acre</h1>
                        <p>{crop} — {year}</p>
                    </div>
                    """, unsafe_allow_html=True)

            else:
                st.error("❌ FastAPI request failed. Check your backend server.")

        except Exception as e:
            st.error(f"⚠️ Error contacting model: {e}")

# TAB 2: About Model
with tab2:
    st.header("The Challenge of Predicting Crop Yields")
    
    st.markdown("""
    <div class="info-box">
    <p>Agriculture has always been a balancing act between human effort and nature's unpredictability. 
    Modern farmers face an increasingly complex set of challenges: <strong>erratic rainfall patterns</strong>, 
    <strong>rising temperatures</strong>, and <strong>pest pressures</strong> that threaten food security 
    across the Caribbean region.</p>
    <p>This dashboard harnesses the power of machine learning to decode these complex relationships, enabling 
    stakeholders to make <strong>data-driven decisions</strong> about agricultural planning, resource allocation, 
    and climate adaptation strategies.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Challenge cards with icons
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="challenge-card">
        <div style="font-size: 3rem;">🌧️</div>
        <h4>Rainfall Variability</h4>
        <p>Unpredictable precipitation patterns affecting planting and harvest cycles</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="challenge-card">
        <div style="font-size: 3rem;">🌡️</div>
        <h4>Temperature Stress</h4>
        <p>Rising temperatures impacting crop development and yield potential</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="challenge-card">
        <div style="font-size: 3rem;">🐛</div>
        <h4>Pest & Disease</h4>
        <p>Managing pesticide use while protecting crops from infestations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="challenge-card">
        <div style="font-size: 3rem;">⚠️</div>
        <h4>Climate Extremes</h4>
        <p>Hurricanes, droughts, and floods threatening Caribbean agriculture</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Jamaica Focus Section
    st.markdown("""
    <div class="badge">Jamaica Focus</div>
    <h3>Jamaica's Agricultural Vulnerability</h3>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <p>Jamaica faces unique challenges as a small island developing state (SIDS). The country's agricultural 
    sector is particularly vulnerable to <strong>hurricane seasons</strong>, <strong>prolonged droughts</strong>, 
    and <strong>shifting rainfall patterns</strong>. Understanding how these factors interact with farming practices 
    is crucial for ensuring food security and supporting rural livelihoods.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project Objectives
    st.markdown("""
    <div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;">
        <span style="font-size: 2rem; margin-right: 1rem;">🎯</span>
        <h2 style="margin: 0;">Project Objectives</h2>
    </div>
    """, unsafe_allow_html=True)
    
    obj_col1, obj_col2 = st.columns(2)
    
    with obj_col1:
        st.markdown("""
        <div class="objective-card">
            <div class="objective-number">1</div>
            <div>
                <h4 style="margin: 0 0 0.5rem 0; color: #3d4f3d;">Develop a Supervised ML Model</h4>
                <p style="color: #7a8a7a; margin: 0;">Build and compare machine learning models (Linear Regression, 
                Random Forest) to predict crop yields based on climate and agricultural inputs.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="objective-card">
            <div class="objective-number">3</div>
            <div>
                <h4 style="margin: 0 0 0.5rem 0; color: #3d4f3d;">Enable Scenario Forecasting</h4>
                <p style="color: #7a8a7a; margin: 0;">Allow users to input custom climate scenarios and predict 
                expected yields under different environmental conditions.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with obj_col2:
        st.markdown("""
        <div class="objective-card">
            <div class="objective-number">2</div>
            <div>
                <h4 style="margin: 0 0 0.5rem 0; color: #3d4f3d;">Understand Yield Drivers</h4>
                <p style="color: #7a8a7a; margin: 0;">Identify and quantify the key factors—rainfall, temperature, 
                pesticide usage—that most significantly influence agricultural productivity.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="objective-card">
            <div class="objective-number">4</div>
            <div>
                <h4 style="margin: 0 0 0.5rem 0; color: #3d4f3d;">Inform Agricultural Policy</h4>
                <p style="color: #7a8a7a; margin: 0;">Provide data-driven insights to support policymakers in 
                developing climate-resilient agricultural strategies for Jamaica and the Caribbean.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)



# Footer
st.markdown("---")
st.markdown("**Crop Yield Prediction Dashboard** | Built with Streamlit | AAI4001 Final Project Group 4")