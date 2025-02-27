from talon import Context, speech_system
from talon.engines.webspeech import WebSpeechEngine

webspeech = WebSpeechEngine()
speech_system.add_engine(webspeech)

# Set the default engine
ctx = Context()
ctx.settings = {
    "speech.engine": "wav2letter",
}
