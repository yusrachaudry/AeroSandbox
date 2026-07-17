# app/ai_advisor.py

def get_ai_recommendation(mission):

    if mission["title"] == "Oxygen Leak":

        return """
### 🤖 AI Recommendation

**Situation Analysis**
- Oxygen levels are decreasing rapidly.
- Crew safety is becoming critical.

**Recommended Action**
✅ Activate backup oxygen.

**Reason**
This action restores life support while the crew locates and repairs the leak.
"""

    elif mission["title"] == "Dust Storm":

        return """
### 🤖 AI Recommendation

**Situation Analysis**
- A severe dust storm is approaching.
- Solar power generation and visibility will decrease.

**Recommended Action**
✅ Wait for instructions from Earth.

**Reason**
Mission Control can evaluate weather data while the crew remains safely inside the habitat.
"""

    elif mission["title"] == "Power Failure":

        return """
### 🤖 AI Recommendation

**Situation Analysis**
- Battery Bank 2 has failed.
- Remaining power must be conserved.

**Recommended Action**
✅ Activate backup oxygen.

**Reason**
Backup life-support systems reduce immediate risk while engineers troubleshoot the electrical failure.
"""

    return "No recommendation available."