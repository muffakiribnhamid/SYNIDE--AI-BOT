import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import phonenumbers
import wikipedia
from phonenumbers import timezone,geocoder,carrier
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random




def sendemail():
    apppassword = ''
    me = "muffakirpc@gmail.com"
    texttoaudio("Enter Receivers Email ")
    you = input("Enter Receivers Email ")
    texttoaudio("Enter Subject")
    email_body = input("Enter Subject")

    message = MIMEMultipart('alternative', None, [MIMEText(email_body, 'html')])

    message['Subject'] = 'Test email send'
    message['From'] = me
    message['To'] = you

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(me, apppassword)
        server.sendmail(me, you, message.as_string())
        server.quit()
        print(f'Email sent: {email_body}')
    except Exception as e:
        print(f'Error in sending email: {e}')

def numberdetails():

    say = texttoaudio("Enter Your Phone Number with Country Code")
    user = record().lower()
    phone = phonenumbers.parse(user)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone, "en")
    reg = geocoder.description_for_number(phone, "en")

    texttoaudio(f"You are from {reg} \nYour Carrier is {car} \nYour Timezone is {time} \nand Your Number is {user}")

def flipcoin():
    c = random.randint(1,2)
    if c == 1:
        texttoaudio("Its Heads")
    elif c == 2:
        texttoaudio("Its Tails")



def record():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Synide Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing.....")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("I didn't understand that sorry")
def wiki():
    texttoaudio("According to wikipedia")
    info = wikipedia.summary(data1)
    print(info)
    texttoaudio(info)
    try:
        texttoaudio("Finding!!")
    except:
        texttoaudio("IDK Sorry")

def texttoaudio(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':


        while True:
          data1 = record()
          if "name" in data1:
              texttoaudio("My Name is Synide")
          elif "developed" in data1:
              texttoaudio("I am developed by Muffakir")
          elif "time" in data1:
              time = datetime.datetime.now().strftime("%I%M%p")
              texttoaudio(time)
          elif "joke" in data1:
              joke = pyjokes.get_joke("en",'neutral')
              texttoaudio(joke)
          elif "youtube" in data1:
              texttoaudio("Opening")
              webbrowser.open("youtube.com")
          elif "facebook" in data1:
              texttoaudio("Opening")
              webbrowser.open("facebook.com")
          elif "twitter" in data1:
              texttoaudio("Opening")
              webbrowser.open("twitter.com")
          elif "instagram" in data1:
              texttoaudio("Opening")
              webbrowser.open("instagram.com")
          elif "song" in data1:
              webbrowser.open("https://www.youtube.com/watch?v=mEdMUvf2mRs&ab_channel=IndianMusic")
          elif "number details" in data1:
              numberdetails()
          elif "exit" in data1:
              texttoaudio("Thanks For Using Me")
              break
          elif "email" in data1:
              sendemail()
              texttoaudio("Email Sent")
          elif "whatsapp" in data1:
              texttoaudio("Enter Number")
              number = input("Enter Number")
              webbrowser.open(f"wa.me/{number}")
          elif "coin" in data1:
              flipcoin()
          elif "what can you do" in data1:
              texttoaudio("I Can PLay songs for You Send Emails send messages open any site give you information of any number Tell You a joke etc. ")
          elif "what" or "mean" or "information" or "about" or "summary" or "knowledge":
              wiki()

          else:
              texttoaudio("I Dont Know About That Sorry")





