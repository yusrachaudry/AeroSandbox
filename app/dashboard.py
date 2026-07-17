# app/dashboard.py

import streamlit as st


def show_dashboard(mission):

    st.title("🚀 Mars Mission Control Dashboard")

    st.markdown("---")

    st.subheader("🛰️ Mission Status")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Mission Day", "42")

    with col2:
        st.metric("Crew", "4")

    with col3:
        st.metric("Location", "Mars Habitat Alpha")

    st.markdown("---")

    st.subheader("🧪 Life Support Systems")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🫁 Oxygen", f"{mission['oxygen']}%")

    with col2:
        st.metric("🔋 Power", f"{mission['power']}%")

    with col3:
        st.metric("🌡️ Temperature", f"{mission['temperature']}°C")

    st.markdown("---")

    st.subheader(f"{mission['icon']} Emergency Scenario")

    st.warning(mission["message"]) 