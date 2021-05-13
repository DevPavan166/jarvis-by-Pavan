import pyttsx3
import speech_recognition as sr #tamare install nai hoy, use this command "pip install speechRecognition"
import datetime
import wikipedia #tamare install nai hoy, use this command "pip install wikipedia"
import webbrowser
import os
import smtplib
from gtts import gTTS
import warnings
import calendar


#pip

warnings.filterwarnings('ignore')

#record audio and return it as a d=string
def recodAudio():

    #record the audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print ("say something......")
         audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
        print('you said: '+data)
    except sr.UnknownValueError:
        print('google speech recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print("request result from google speech recognition service error" + e )
    return data

def assistantResponse(text):

    print(text)
    myobj = gTTS(text= text, lan='en', slow=false)

    myobj.save('assistant_response.mp3')

    os.system('start assistant_response.mp3')


def wakeword(text):
        WAKE_WORDS = ['hey computer', 'okay computer', 'hello computer']

        text = text.lower()

        for phrase in WAKE_WORDS:
            if phrase in text:
                return True

        return False

def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January','Feburary', 'March', 'April', 'May', 'Jun', 'July', 'August', 'September',
                   'October', 'November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                      '14th', '15', '16th', '17th', '17th', '18th', '19th', '20th', '21th', '22th', '23th', '24th',
                      '25th', '26th', '27th', '28th', '29th', '30th', '31th']

    return 'Today is ' +weekday+' '+ month_names[monthNum - 1]+' the '+ ordinalNumbers[dayNum -1]+'. '


def greeting(text):

    GREETING_INPUTS = ['hello', 'hi', 'hello laptop', 'hey']

    GREETING_RESPONSES = ['howdy', 'whats good', 'hell0', 'hey there']

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) +'. '

        return ' '

def getPerson(text):

    wordList = text.split()

    for i in range(0 , len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' '+ wakeword[i+3]

while True:

    text = recodAudio()
    response = ' '


    if(wakeword() == True):

        response = response + greeting(text)

        if('date' in  text):

            get_date = getDate()
            response = response+ ' '+ get_date

        if('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response+ ' '+ wiki

        assistantResponse(response)

















