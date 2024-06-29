import pyttsx3                                    
import datetime                                   
import speech_recognition as sr                   
import wikipedia                                  
import webbrowser                                 
import os.path                                    
import smtplib                                    
import os


engine = pyttsx3.init('sapi5')                    
voices = engine.getProperty('voices')             
engine.setProperty('voice', voices[1].id)          


def speak(audio):                               
    engine.say(audio)
    engine.runAndWait()                         


def wish_me():                                    
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('Hello Sir, I am Buddy, your artificial intelligence assistant. Please tell me how may I help you')


def take_command():                               
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)

    try:                                            
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')  
        print(f'User said: {query}\n')
    except Exception as e:
        print('Say that again please...')        
        return 'None'  
    return query.lower()

def send_email(to, content):                       
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        sender_email = os.getenv('SENDER_EMAIL')
        sender_password = os.getenv('SENDER_PASSWORD')
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, content)
        server.close()
        speak('Email has been sent')
    except Exception as e:
        print(e)
        speak('Sorry, I am not able to send this email')


if __name__ == '__main__':                   
    wish_me()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=5)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            speak('Okay boss')
            music_dir = 'path_to_your_music_directory'
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak('No music files found in the directory')

        elif 'time' in query:
            str_time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {str_time}')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'email' in query:
            try:
                speak('What should I write in the email?')
                content = take_command()
                to = 'receiver_email@gmail.com'
                send_email(to, content)
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email')

        elif 'exit' in query:
            speak('Okay boss, please call me when you need me')
            break

