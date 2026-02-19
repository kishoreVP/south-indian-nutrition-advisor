"""
Configuration for Smart Nutrition Advisor using Gemini
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Gemini API key

# Messaging Configuration (unchanged)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL", "nutrition@yourapp.com")

# Model Configuration
DEFAULT_MODEL = "gemini-2.5-flash"
TEMPERATURE = 0

# Available Gemini Models:
# - gemini-1.5-pro: Best for complex reasoning
# - gemini-1.5-flash: Faster, good for most tasks
# - gemini-pro: Standard model

# Nutritional Guidelines (daily recommended values)
DAILY_LIMITS = {
    "diabetes": {
        "calories": 1800,
        "carbs": 200,  # grams
        "sugar": 25,
        "fiber_min": 25
    },
    "hypertension": {
        "sodium": 2300,  # mg (ideally 1500)
        "calories": 2000
    },
    "obesity": {
        "calories": 1500,
        "fat": 50
    },
    "kidney_disease": {
        "protein": 50,  # varies by stage
        "potassium": 2000,
        "phosphorus": 1000,
        "sodium": 2000
    }
}

# Messaging Templates
SMS_TEMPLATE = """Hi {name}! 

Your nutrition analysis is ready.

⚠️ Key concerns:
{concerns}

✅ Recommendations:
{recommendations}

Check your email for details!
"""

EMAIL_SUBJECT_TEMPLATE = "Your Nutrition Report - {date}"

REMINDER_TEMPLATE = """Hi {name}!

Time for {meal}! Remember:
{tips}

Stay healthy! 💪
"""