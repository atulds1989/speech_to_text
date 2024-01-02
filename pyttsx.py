# # Python program to translate
# # speech to text and text to speech

# import speech_recognition as sr
# import pyttsx3

# # Initialize the recognizer
# r = sr.Recognizer()

# # Function to convert text to
# # speech
# def SpeakText(command):
#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()


# # Loop infinitely for the user to speak
# while True:
#     # Exception handling to handle
#     # exceptions at runtime
#     try:
#         # use the microphone as a source for input.
#         with sr.Microphone() as source2:

#             # wait for a second to let the recognizer
#             # adjust the energy threshold based on
#             # the surrounding noise level
#             r.adjust_for_ambient_noise(source2, duration=0.2)

#             # listens for the user's input
#             audio2 = r.listen(source2)

#             # Using google to recognize audio
#             MyText = r.recognize_google(audio2)
#             MyText = MyText.lower()

#             print("Did you say ", MyText)
#             SpeakText(MyText)

#             # Break the loop if the phrase "stop listening" is detected
#             if "stop listening" in MyText:
#                 print("Stopping the loop...")
#                 break

#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))

#     except sr.UnknownValueError:
#         print("Unknown error occurred")



###############################################



import speech_recognition as sr
import pyttsx3
import keyboard

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Initialize a flag for the loop
keep_listening = True

# Loop infinitely for the user to speak
while keep_listening:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say ", MyText)
            SpeakText(MyText)

            # Check for a key press to set the flag and break the loop
            if keyboard.is_pressed('q'):
                print("Key 'q' pressed. Stopping the loop...")
                keep_listening = False

            # Break the loop if the phrase "stop listening" is detected
            if "stop listening" in MyText:
                print("Stopping the loop...")
                keep_listening = False

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occurred")
