# Text-to-Speech with gTTS

This project demonstrates a simple **Text-to-Speech (TTS)** implementation in Python using [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/).
It converts text into natural-sounding speech, saves it as an MP3 file, and plays the audio automatically.

---

## Installation

1. Clone this repository or copy the script.

   ```bash
   git clone https://github.com/akritisshetty/text-to-speech-using-gTTS.git
   cd text-to-speech-gtts
   ```
2. Install dependencies:

   ```bash
   pip install gTTS
   ```
3. (Optional) For direct playback inside Python:

   ```bash
   pip install playsound
   ```

---

## Cross-Platform Notes

* **Linux/macOS** → uses `xdg-open` / `open` to play the MP3 file.
* **Windows** → replace with:

  ```python
  os.system(f"start {filename}")
  ```
* With `playsound`, playback works the same across all platforms:

  ```python
  from playsound import playsound
  playsound(filename)
  ```
