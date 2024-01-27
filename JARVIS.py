import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import cv2
import random
import wikipedia
from requests import get
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui 
import requests
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)
#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#voice to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source,timeout=2,phrase_time_limit=5)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}")  
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query
#to wish
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning sir")
    elif hour>12 and hour<=18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("I am Jarvis I am here to help You")
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("madhupiska1002@gmail.com","tezv ecsh hmvg jveh")
    server.sendmail("your email id",to, content)
    server.close()
def news():
    main_url="http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=9f97d37bce94460d9c60a4d1fe478b63"
    main_page=requests.get(main_url).json()
    #print mainpage
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        #print(f"today's {day[i]} news is:" , head[i])
        speak(f"today's {day[i]} news is:  {head[i]}")
if __name__=="__main__":
    wish()
    while True:
        query=takecommand().lower()
        #logic building for tasks
        if "open notepad" in query:
            path="C:\\Windows\\notepad.exe"
            os.startfile(path)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow("webcam",img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music="D:\\songs"
            songs=os.listdir(music)
            rand=random.choice(songs)
            os.startfile(os.path.join(music,rand))
        elif "ip address" in query:
                ip=get("https://api.ipify.org").text
                speak(f"{ip} is your IP Address")
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=4)
            speak("according to wikipedia")
            speak(result)
            print(result)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "open whatsapp web" in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif "open github" in query:
            webbrowser.open("www.github.com")
        elif "open google" in query:
            speak("what shall i search on google sir")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+918686057576","this is hero panthi verey untadi python jarvis message cheste",16,33)
        elif "play songs on youtube" in query:
            kit.playonyt("star boy")
        elif "send email to tarun" in query:
            speak("sir what should i send")
            query=takecommand().lower()
            if "send a file" in query:
                email="madhupiska1002@gmail.com"#your mail
                password="123Madhu@!@!##"
                send_to_mail="madhupiska2000@gmail.com"
                speak("okay sir what is the subject for this email")
                query=takecommand().lower()
                subject=query
                speak("and sir what is the message for this email")
                query2=takecommand().lower()
                message=query2
                speak("please enter the correct path of the file into the shell")
                file_location=input("please enter the file location here")
                speak("please wait sir, I am sending email now")
                msg=MIMEMultipart()
                msg["From"]=email
                msg["To"]=send_to_mail
                msg["subject"]=subject
                msg.attach(MIMEText(message,"plain"))
                #setup the attachment
                filename=os.path.basename(file_location)
                attachment=open(file_location,"rb")
                part=MIMEBase("application","octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("content-Dispostion","attachment; filename=%s"%filename)
                #attach the attachment to MIMEMultipart object
                msg.attach(part)
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(email,"tezv ecsh hmvg jveh")
                text=msg.as_string()
                server.sendmail(email,send_to_mail, text)
                server.quit()
                speak("email has been sent to tharun")
            else:
                email="madhupiska1002@gmail.com"
                password="123Madhu@!@!##"
                send_to_mail="madhupiska2000@gmail.com"
                message=query
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(email,"tezv ecsh hmvg jveh")
                server.sendmail(email,send_to_mail, message)
                server.quit()
                speak("email has been sent to tharun")
        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day")
        elif "close notepad" in query:
            speak("okay sir closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif "set alarm" in query:
            m=int(datetime.datetime.now.hour())
            if(m==17):
                music="D:\\songs"
                songs=os.listdir(music)
                os.startfile(os.path.join(music,songs[1]))
        elif "tell me a joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)
        elif "shutdown" in query:
            os.system("shutdown/s/t/5")
        elif "restart the computer" in query:
             os.system("shutdown/s/t/5")
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif "switch the window" in query:
            pyautogui.keyDown("altś")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()
        elif "you can sleep" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()
        speak("do you have any other work")