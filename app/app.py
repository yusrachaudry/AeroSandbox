import streamlit as st
import scenarios

from ai_advisor import get_ai_recommendation
from dashboard import show_dashboard
from logger import initialize_csv, save_result

# -----------------------------
# Page Settings
# -----------------------------
st.set_page_config(
    page_title="Mars AI Decision Support",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Initialize CSV
# -----------------------------
initialize_csv()

# -----------------------------
# New Mission
# -----------------------------
if "mission" not in st.session_state:
    st.session_state.mission = scenarios.get_random_scenario()

mission = st.session_state.mission

# -----------------------------
# Dashboard
# -----------------------------
show_dashboard(mission)

st.divider()

# -----------------------------
# Participant Information
# -----------------------------
st.header("👤 Participant")

participant = st.text_input(
    "Participant ID",
    placeholder="Example: P001"
)

# -----------------------------
# AI Advisor
# -----------------------------
st.header("🤖 AI Mission Advisor")

if st.button("Ask AI Recommendation"):
    recommendation = get_ai_recommendation(mission)
    st.info(recommendation)

# -----------------------------
# Crew Decision
# -----------------------------
st.header("📝 Crew Decision")

decision = st.radio(
    "Choose the best action:",
    [
        "Ignore warning",
        "Activate backup oxygen",
        "Evacuate habitat",
        "Wait for instructions from Earth"
    ]
)

confidence = st.slider(
    "How confident are you?",
    1,
    5,
    3
)

# -----------------------------
# Submit Decision
# -----------------------------
if st.button("Submit Decision"):

    if participant.strip() == "":
        st.error("⚠️ Please enter a Participant ID.")
    else:

        save_result(
            participant,
            mission["title"],
            decision,
            confidence
        )

        if decision == mission["correct_answer"]:
            st.success("✅ Decision saved. Your decision matches the recommended action.")
        else:
            st.warning("⚠️ Decision saved. Your decision differs from the recommended action.")

# -----------------------------
# Download Results
# -----------------------------
st.divider()

try:
    with open("data/results.csv", "rb") as file:
        st.download_button(
            label="📥 Download Research Results",
            data=file,
            file_name="mars_research_results.csv",
            mime="text/csv"
        )
except FileNotFoundError:
    st.info("No research results have been collected yet.")

# -----------------------------
# New Mission
# -----------------------------
if st.button("🚀 Generate New Mission"):
    st.session_state.mission = scenarios.get_random_scenario()
    st.rerun()