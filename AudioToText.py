import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def Speech_to_text():
    with microphone as source:
        print("Listening for audio...")

        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data)
            # text = recognizer.recognize_google(audio_data)
            print("Text converted from audio:", text)
            print(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


