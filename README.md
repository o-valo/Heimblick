# Heimblick - Vision App 👁️

[Deutsch](#deutsch) | [English](#english) | [Installation & Setup](#setup)

---

<a name="deutsch"></a>
## 🇩🇪 Deutsch: Heimblick – Der Blindenstock 2.0

Heimblick ist eine innovative Vision-App, die speziell für Menschen mit Sehbehinderungen oder Blindheit entwickelt wurde. Ziel des Projekts ist es, die Welt der Sehenden durch den Einsatz von Künstlicher Intelligenz (KI) akustisch erlebbar zu machen.

### Die Vision
Hinter Heimblick steht die Idee für Menschen, die nicht so gut sehen können oder blind sind, eine Möglichkeit zu schaffen, mehr von der Welt der Sehenden zu erfahren. Die App bietet eine wertvolle Orientierungshilfe im Alltag.

### Funktionsweise
1. **Bildaufnahme:** Die Kamera erfasst die Umgebung.
2. **KI-Analyse:** Ein LLM-Vision-Modell analysiert das Bild.
3. **Audio-Feedback:** Die Beschreibung wird zurückgegeben und dem Nutzer laut vorgelesen.

### Status
Heimblick ist aktuell ein Prototyp, welcher weiterentwickelt werden soll, um später als Blindenstock 2.0 arbeiten zu können.

---

<a name="english"></a>
## 🇺🇸 English: Heimblick – The White Cane 2.0

Heimblick is an innovative vision app designed to support people with visual impairments or blindness. The project's goal is to make the "world of the sighted" acoustically perceivable through the use of Artificial Intelligence (AI).

### The Vision
The core idea behind Heimblick is to create a bridge between the visual world and individuals with limited or no vision. It provides a valuable navigational and descriptive aid for daily life.

### How it Works
1. **Image Capture:** The camera captures the surroundings.
2. **AI Analysis:** An LLM Vision Model (via Ollama) analyzes the image in real-time.
3. **Audio-Feedback:** The description is sent back and read aloud to the user.

---

<a name="setup"></a>
## 🛠️ Installation & Setup (DE/EN)

### 1. Requirements / Voraussetzungen

**DE:** Um Heimblick zu nutzen, benötigen Sie eine aktive Verbindung zur Ollama API.
* **Hardware:** Ein Gerät mit Kamera und Zugriff auf ein Ollama-Backend, das Vision-LLMs unterstützt.
* **Software:** Ollama muss installiert und über das Netzwerk erreichbar sein.

**EN:** To use Heimblick, you need a working Ollama API connection.
* **Hardware:** A device with a camera and access to an Ollama backend capable of running Vision LLMs.
* **Software:** Ollama installed and reachable via network.

* Beispiel Modell / Example Model   :

### 2. Configuration / Konfiguration

**DE:** Passen Sie die folgenden Variablen im Skript an Ihr Netzwerk-Setup an:
**EN:** Update the following variables in your script to match your network setup:

**Ollama API Endpoint:**
```python
OLLAMA_URL = "http://YOUR-IP-HERE:11434/api/generate"

MODEL_NAME = "aha2025/llama-joycaption-beta-one-hf-llava:Q4_K_M"

```
3. Usage / Nutzung

DE: Sobald die Konfiguration abgeschlossen ist, nimmt die App ein Bild auf, sendet es an den Ollama-Server und das Vision-Modell beschreibt akustisch, was es sieht.

EN: Once configured, the app takes a picture, sends it to the Ollama server, and the Vision model describes what it sees.
