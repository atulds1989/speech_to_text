# Import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# Listening to the speech and store it in the audio_text variable
with sr.Microphone() as source:
    print("Talk")

    try:
        # Listen for up to 10 seconds
        audio_text = r.listen(source, timeout=10)
        print("Time over, thanks")

        # Using Google Speech Recognition
        print("Text: " + r.recognize_google(audio_text))
    except sr.WaitTimeoutError:
        print("Timed out. No speech detected.")
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
