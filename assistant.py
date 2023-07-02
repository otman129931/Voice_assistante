
import speech_recognition as sr
import wikipedia
import pyttsx3
from datetime import datetime
import time

class Helper:
    #initializing speech engine 
    activationword=['liza', 'lisa','hello', 'hi']
    def __init__(self):
        global assistant, activationword
        assistant=pyttsx3.init()
        voices=assistant.getProperty('voices')
        assistant.setProperty('voice', voices[1].id)
        
    def speak(self, text, rate=120):
        assistant.setProperty('rate', rate)
        assistant.say(text)
        assistant.runAndWait()
    def parscommand(self):
        listner=sr.Recognizer()
        print('Listning.............')
        with sr.Microphone() as source:
            listner.pause_threshold=2
            input_speech= listner.listen(source)
        try:
            print('Recognizing speech ............')
            query=listner.recognize_google(input_speech, language='en_gb')
            print(f'the speech regognizerd was : {query}')
        except Exception as exception:
            print(' i did not catche a speech')
            self.speak(' i did not catche a speech')
            print(exception)
            return 'None'
        return query
    def search_wikipedia(self, keyword=''):
        searchResults = wikipedia.search(keyword)
        if not searchResults:
            return 'No result received'
        try: 
            wikiPage = wikipedia.page(searchResults[0]) 
        except wikipedia.DisambiguationError as error:
            wikiPage = wikipedia.page(error.options[0])
        print(wikiPage.title)
        wikiSummary = str(wikiPage.summary)
        return wikiSummary
  