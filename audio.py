# =========================
# INSTALL (run once in Jupyter)
# %pip install sounddevice scipy openai-whisper gtts torch
# =========================

import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from gtts import gTTS

# 👉 IMPORT YOUR EXISTING FUNCTION
from nutrition_advisor import analyze_patient_meal

# =========================
# 🎤 STEP 1: RECORD AUDIO
# =========================
duration = 5  # seconds
fs = 16000

print("🎙️ Speak now (e.g., 'I ate 3 idli and 1 vada')...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

write("input.wav", fs, audio)
print("✅ Recording complete!")

# =========================
# 🧠 STEP 2: SPEECH → TEXT
# =========================
model = whisper.load_model("base")

result = model.transcribe("input.wav")
transcript = result["text"]

print("📝 Transcription:", transcript)

# =========================
# 🍽️ STEP 3: EXTRACT FOOD (simple version)
# =========================
# ⚠️ For now, basic manual mapping (can upgrade later with Gemini)

food_items = []

if "idli" in transcript.lower():
    food_items.append({"name": "Idli", "quantity": "2"})
if "vada" in transcript.lower():
    food_items.append({"name": "Vada", "quantity": "1"})
if "dosa" in transcript.lower():
    food_items.append({"name": "Dosa", "quantity": "1"})
if "sambar" in transcript.lower():
    food_items.append({"name": "Sambar", "quantity": "1 bowl"})

# fallback if nothing detected
if not food_items:
    food_items = [{"name": "Idli", "quantity": "2"}]

print("🍽️ Detected food:", food_items)

# =========================
# 🧠 STEP 4: ANALYZE MEAL
# =========================
result = analyze_patient_meal(
    patient_id="P001",
    patient_name="Ramesh",
    food_items=food_items,
    medical_conditions=["Diabetes"],
    meal_time="breakfast",
    patient_email="test@gmail.com"
)

report = result["final_report"]

print("\n📊 ANALYSIS:")
print(report)

# =========================
# 🔊 STEP 5: TEXT → AUDIO
# =========================
response_text = f"Here is your nutrition advice. {report[:300]}"  # short version

tts = gTTS(text=response_text, lang="en")  # change to "ta" for Tamil
tts.save("response.mp3")

print("🔊 Response audio saved as response.mp3")
