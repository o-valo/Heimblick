import cv2
import base64
import requests
import json

# Ollama API-Endpunkt
OLLAMA_URL = "http://10.7.0.86:11434/api/generate"

# Modellname
MODEL_NAME = "aha2025/llama-joycaption-beta-one-hf-llava:Q4_K_M"

# Funktion zum Aufnehmen eines Bildes mit OpenCV
def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Kann Kamera nicht öffnen")

    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise Exception("Kann kein Bild aufnehmen")

    # Speichern des Bildes temporär (optional, wir nutzen Base64)
    _, buffer = cv2.imencode('.jpg', frame)
    img_b64 = base64.b64encode(buffer).decode('utf-8')
    return img_b64

# Funktion zum Senden der Anfrage an Ollama mit Streaming
def send_to_ollama(image_b64, prompt="Beschreibe das Bild detailliert."):
    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [image_b64],
        "stream": True  # Streaming aktivieren
    }

    response = requests.post(OLLAMA_URL, json=data, stream=True)

    full_response = ""
    for line in response.iter_lines():
        if line:
            decoded = line.decode('utf-8')
            try:
                parsed = json.loads(decoded)
                if 'response' in parsed:
                    full_response += parsed['response']
                    print(parsed['response'], end='', flush=True)
            except json.JSONDecodeError:
                pass  # Ignoriere ungültige JSON-Zeilen

    print("\n" + "="*50)
    print("Vollständige Antwort:")
    print(full_response)
    print("="*50)

# Hauptprogramm
if __name__ == "__main__":
    try:
        print("🚀 Starte Vision-Analyse...")
        print("--- 1. Bilderfassung ---")
        image_b64 = capture_image()
        print("✅ Bild erfolgreich aufgenommen und kodiert.")

        print("\n--- 2. Sende an Ollama ---")
        send_to_ollama(image_b64)

    except Exception as e:
        print(f"❌ Fehler: {e}")
