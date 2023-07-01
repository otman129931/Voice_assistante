
import speech_recognition as sr
import wikipedia
import pyttsx3
from datetime import datetime
import time

#initializing speech engine 
assistant=pyttsx3.init()
voices=assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)
activationword=['liza', 'lisa','hello', 'hi']
def speak(text, rate=120):
    assistant.setProperty('rate', rate)
    assistant.say(text)
    assistant.runAndWait()

def parscommand():
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
        speak(' i did not catche a speech')
        print(exception)
        return 'None'
    return query
def search_wikipedia(keyword=''):
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
if __name__ == '__main__': 
    speak('Hi I am liza your assistante. i can search on wikipedia and write some note for you, how can i help you ', 140)

    while True:

        query = parscommand().lower().split()

        if query[0] in activationword and len(query) > 1:
            query.pop(0)
             # Wikipedia
            if 'wikipedia' in query:
                pos= [ind for ind, v in enumerate(query) if v == 'wikipedia' ]
                query = ' '.join(query[pos[0]:])
                speak('Querying the universal databank')
                time.sleep(2)
                speak(search_wikipedia(query))
            # Note taking
            if query[0] == 'note':
                speak('Ready to record your note')
                newNote = parscommand().lower()
                now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(now)
                    newFile.write(' ')
                    newFile.write(newNote)
                speak('Note written')
            if query[0] == 'bye':
                speak('Goodbye')
                break

