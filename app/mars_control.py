import streamlit as st

# Page title
st.title("🚀 Mars Mission Control Dashboard")

# Mission Information
st.header("Mission Status")

st.write("Mission Day: 42")
st.write("Location: Mars Habitat Alpha")
st.write("Crew Members: 4 Astronauts")

# System Monitoring
st.header("Life Support Systems")

oxygen = 72
power = 91
temperature = -63

st.metric("🫁 Oxygen Level", f"{oxygen}%")
st.metric("🔋 Power Level", f"{power}%")
st.metric("🌡️ Outside Temperature", f"{temperature}°C")


# Emergency Alert
st.header("🚨 Emergency Alert")

st.warning(
    "Oxygen pressure is decreasing. Immediate action required."
)


# Crew Decision
st.header("Crew Decision")

choice = st.radio(
    "What action should the crew take?",
    [
        "Ignore warning",
        "Activate backup oxygen",
        "Evacuate habitat",
        "Wait for instructions from Earth"
    ]
)


if st.button("Submit Decision"):
    st.success(f"Decision recorded: {choice}")