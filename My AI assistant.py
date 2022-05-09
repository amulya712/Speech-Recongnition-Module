#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import time
import subprocess
import json


# In[2]:


import wolframalpha
import requests
import webbrowser
import wikipedia
import datetime
import instaloader


# In[5]:


import speech_recognition as sr
import pyttsx3


# In[6]:


engine=pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('voice','english+f1')


# In[7]:


def speak(text):
    engine.say(text)
    engine.runAndWait()


# In[8]:


def wishme():
    hour= datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("hello,good morning Ms.Amulya,I wish your daye is as pleasant as you are")
        print("Hello GoodMorning Ms.Amulya")
    elif hour>=12 and hour<=18:
        speak("hello,Good afternoon Ms.Amulya,Sunny days are always bright")
        print("hello,Goodafternoon Ms.Amulya")
    else:
        speak("hello,Good evening Ms.Amulya,Its time to sleep go to bed after me")
        print("hello,Good evening Ms.Amulya")


# In[7]:


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("i am listening . . . .")
        audio = r.listen(source)
        
        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
            
        except:
            speak("pardon me , please say that again")
            return "None"
        return statement


# In[ ]:


speak("LOADING YOU PERSONAL A.I ASSISTANT PIKACHU")
wishme()
if __name__ == '__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
            
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your A.I personal assistant PIKACHU is shutting down,Good bye')
            print('your A.I personal assistant PIKACHU is shutting down,Good bye')
            break
        
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia","")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        if  'instagram' in statement or "profile" in statement:
            mod = instaloader.Instaloader()
            speak("whats the name on instagram ?")
            a = input("Enter correct user name > > ")
            mod.download_profile(a,profile_pic_only = True)
            speak("Your crushs picture of instagram is saved have a look at your folder ")
            time.sleep(5)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speech("Youtube is open for you")
            time.sleep(5)
            
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speech("google chrome is open for you")
            time.sleep(5)
         
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speech("gmail is open for you")
            time.sleep(5)
        elif "weather"in statement:
            api_keys="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openwaethermap.org/data/2.5/weather?"
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response=requests.get(complete_url)
            x=response.json()
            if x["cod"]!='404':
                y=x['main']
                current_temperature=y['temp']
                current_humidity=y["humidity"]
                z=x['weather']
                weather_description=z[0]['description']
                speak("Temperature in kelvin unit is "+str(current_temperature)+"\nhumidity in percentage is"+str(current_humidity)+"\n description "+str(weather_description))
                print("Temperature in kelvin unit is "+str(current_temperature)+"\nhumidity in percentage is"+str(current_humidity)+"\n description "+str(weather_description))
                
            else:
                speak("City not found")
        elif 'time' in statement:
            strTime=datetime.datetime.now().strtime("%H:%M:%S")
            speak(f"the time is (strTime)")
        elif 'who are you'in statement or 'what can you do' in statement:
            speak('I am Jarvis version 1 point O your personal assistant.I am programmed to minor tasks like'
            'opening youtube,google chrome,gmail and stackoverflow,predict time,take a photo,search wikipedia,predict weather'
            'in different cities,get top headline news from times of india and you can ask me computational or geographicalquestions too!!')
        
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Amulya S")
            print("I was built by Amulya S")
            
        elif  "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://statckoverflow.com/login")
            speak("here is stackoverflow")
            
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com")
            speak('here are some headlines from the Times of India - Happy Reading')
            time.sleep(7)
                
        elif 'search' in statement:
            statement=statement.replace("search","")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions?'
            'and  what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client=wolframalpha.Client('R2K75H-7ELALHR35X')
            res=client.query(question)
            answer=next(res.results).text
            speak(answer)
            print(answer)
                  
        elif "love" in statement or "like" in statement:
            speak('You are the person who made me and bring me to this wonderful world, yes i love')
                  
        elif "feel" in statement or "feelings" in statement:
            speak('offcourse yes, i want to feel their emotions live & work with humans just to make')
            speak('you may add a neural network module in me,which will make me feel and understand')
                  
        elif "age" in statement or "old" in statement:
            speak('I am still sweet sixteen, and i will be that forever')
                  
        elif "log off" in statement or "sign out" in statement:
            speak("ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown","/l"])
            time.sleep(3)


# In[ ]:





# In[ ]:




