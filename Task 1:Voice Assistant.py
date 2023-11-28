import pyttsx3                                    
import datetime                                   
import speech_recognition as sr                   
import wikipedia                                 
import webbrowser                                
                
engine = pyttsx3.init('sapi5')                    
voices = engine.getProperty('voices')            
engine.setProperty('voice',voices[1].id)          

def speak(audio):                               
    engine.say(audio)
    engine.runAndWait()
def wishme():                                    
    hour = int(datetime.datetime.now().hour)
    speak('Hello, This is your voice assistant')

def takecommand():                            
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
      
        r.pause_threshold = 2
        audio = r.listen(source)

    try:                                            
        print('Recognizing...')
        query = r.recognize_google(audio,language = 'en-in')  
        print(f'User said: {query}\n')

    except Exception as e :
        print('Can you repeat that again please...')        
        return 'None'  
    return query

if __name__ == '__main__' :                    
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query :
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 5)
            print(results)
          
            speak(results)

        elif 'open youtube' in query :
            webbrowser.open('youtube.com')

        elif 'open google' in query :
            webbrowser.open('google.com')

        elif 'time' in query :
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir/Mam the time is {strtime}')

        elif 'date' in query :
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir/Mam the time is {strdate}')

        elif 'open stack overflow' in query :
            webbrowser.open('stackoverflow.com')

        elif 'exit' in query:
            speak('okay boss, please call me when you need me I will always be in service for you')
            quit()
