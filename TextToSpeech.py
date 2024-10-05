import io

from gtts import gTTS

def text_to_speech(word, language='en'):
    tts = gTTS(text=word, lang=language, slow=False)

    audio_buffer = io.BytesIO()# instead of saving audio to file we are saving it to buffer and not to disc
    
    tts.write_to_fp(audio_buffer)
    
    audio_buffer.seek(0) 
    return audio_buffer
