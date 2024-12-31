import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("Good Morning my dear friends")
    elif hour >=12 and hour <18:
        speak("Good afternoon my dear friends")
    else:
        speak("Good evening my dear friends")
    speak("Let me know how can I help you, What are you looking for ?")
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you Priya ....")
        r.pause_threshould = 1 #if voice not clear then ask again
        audio = r.listen(source)
        
    try:
        print("Recognizing your voice....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"My dear friend you said : {query}\n")
    
    except Exception as e:
        print("Priya say that again please ....")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) #587 is server
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'emailpassword')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
if __name__ == '__main__':
    wishme()
    
    while True:
        query = takecommand().lower()
        
        if 'open wikipedia' in query:
            speak('Searching wikipedia ....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        if 'open notepad' in query:
            npath ="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            
        elif 'open paint' in query:
            npath = "C:\\Users\\priya\\AppData\\Local\\Microsoft\\WindowsApps\\mspaint.exe"
            os.startfile(npath)
            
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')
            
        elif 'open great learning' in query:
            webbrowser.open("https://www.greatlearning.in/")
            
        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"My dear friend, the time is{strTime}")
            
        elif 'open great learning youtube channel' in query:
            webbrowser.open("https://www.youtube.com/user/beaconelearning")
            
        elif 'open linkedin' in query:
            webbrowser.open("www.linkedin.com")
            
        elif 'email to other friend' in query:
            try:
                speak("What should I send ?")
                content = takecommand()
                to = "ReceiverEmail@gmail.com"
                sendEmail(to, content)
                speak("Your email has been sent successfully")
                
            except Exception as e:
                print(e)
                speak("My dear friend... I am unable to send the email..."
                    "Please address the error...")