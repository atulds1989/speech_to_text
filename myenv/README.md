# Google-speech-to-text-python
Python pyttsx3 which converts input audio stream from microphone to text using Google speech to text

<b>Setup</b>

1) Clone the repo 

    $ git clone https://github.com/atulds1989/speech_to_text.git
2) Install pip and virtualenv if you do not already have them. 
3) Create a virtualenv with Python 3.11.6
4) Install the dependencies
    
    $ pip install -r requirements.txt
    
5) Run

    $ python saved_audio.py # for saved audio to text conversion
    
    $ python microphone.py # for saved audio to text conversion

    $ python pyttsx.py # this file uses pyttsx3 library which uses the microphone to listen the voice then it convert it to the ext form and give a feedback that system recognized correct text from your voice or not in the form of an audio msg.
    