# Converts text to speech and saves it as an MP3 file.

from gtts import gTTS
import os

def text_to_speech(text, lang = 'en', slow = False, filename = 'audio.mp3'):
    """
    Converts text to speech and saves it as an MP3 file.

    :param text: The text to convert to speech.
    :param lang: The language for the speech (set to English).
    :param slow: If True, the speech will be slower (set to False).
    :param filename: The name of the output MP3 file (default is 'audio.mp3').
    """
    tts = gTTS(text = text, lang = lang, slow = slow)
    tts.save(filename)
    print(f"Audio saved as {filename}") 
    # To play the audio file
    os.system(f"xdg-open {filename}")
# Sample usage

if __name__ == "__main__":
    text = "Hello! I am a Text to Speech generator. Nice to meet you!"
    text_to_speech(text, lang = 'en', slow = False, filename = 'audio.mp3')
