import random

SCENARIOS = [
    {
        "title": "Oxygen Leak",
        "icon": "🫁",
        "message": "Oxygen levels are dropping by 2% every minute.",
        "oxygen": 72,
        "power": 91,
        "temperature": -63,
        "correct_answer": "Activate backup oxygen"
    },
    {
        "title": "Dust Storm",
        "icon": "🌪️",
        "message": "A severe dust storm is approaching the habitat.",
        "oxygen": 95,
        "power": 60,
        "temperature": -80,
        "correct_answer": "Wait for instructions from Earth"
    },
    {
        "title": "Power Failure",
        "icon": "⚡",
        "message": "Battery Bank 2 has failed.",
        "oxygen": 88,
        "power": 42,
        "temperature": -55,
        "correct_answer": "Activate backup oxygen"
    }
]

def get_random_scenario():
    return random.choice(SCENARIOS)