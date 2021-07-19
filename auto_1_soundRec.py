import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit
import datetime
import os
import webbrowser
from time import sleep
from PIL import Image, ImageTk
from screat import pw
import pdfplumber
from instagram_bot import instBot
from image_open import my_pics_list_, close_pictures, pdf_read


def open_app():
    os.system("start photoshop.exe")
    

def send_whatsapp():
    now = datetime.datetime.now()
    hour = now.hour
    mininute = now.minute + 1.5
    nazbeeen = f'ilove You Dear, iwant spend my life with you dear proud of you'
    pywhatkit.sendwhatmsg('+234 810 304 3030','{}my love {}'.format( nazbeeen, 'zeenatu_na'), hour, mininute)



def close_app():
    os.system("taskkill /im photoshop.exe /f")


def close():
    browserExe = "chrome.exe" 
    return  os.system("taskkill /f /im "+browserExe) 

def readFile():
    with pdfplumber.open(r'G:\videos\pdf\algebra\Physics.pdf') as pdf:
        first_page = pdf.pages[0]
        print(first_page.extract_text())
        return first_page.extract_text()
           
       


def fn():
    filee_dir = os.listdir(r"G:\Sallah\jega\New folder\New folder")
    return len(filee_dir)


def time(time_now):
    while True:
        return time_now.strftime("%H:%M")
        



r = sr.Recognizer()
engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening.........")
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command = command.lower()
            if 'zinat' in command:
                command = command.replace('zinat', '')
                print(command)
    except Exception as e:
        print(e)
        zeenatu ="say that again sir"
        print(zeenatu)
        return take_command()
    return command

if __name__ == '__main__':
    while True:
        command = take_command()
        if  'play' in command:
            song = command.replace('play', '')
            talk("playing" + song)
            pywhatkit.playonyt(song, 5)
            print(song)
        if 'close ' in command:
            closes = command.replace('close', '')
            talk('okey sir closed Chrome' + closes)
            print(close())      
            continue
        if 'search' in command:
            search = command.replace('open', '')
            talk('searching' + search)
            pywhatkit.search(search)
            print(search)
            continue
        if 'send to my love message' in command:
            text = command.replace('send to my love message', '')
            talk('sending message to my Love' + str(send_whatsapp()))         
            print(text)
            continue
        if 'time' in command:
            time_now = command.replace('time', '')
            talk('sir time is ' + time(datetime.datetime.now()))
            print(time(datetime.datetime.now()))
            continue
        # if 'picture' in command:
        #     folder = command.replace('pictures', '')
        #     talk('sir you have' + str(fn()))
        #     print(fn())
        #     continue
        if 'read' in command:
            folder = command.replace('read', '')
            talk('sir you have' + str(readFile()).extract_text())
            continue
        if 'instagram' in command:
            inst = command.replace('instagram', '')
            talk('instagram opened' + str(instBot("nazbeen_gallery_", pw)))
            continue
        if 'photoshop' in command:
            photoshop = command.replace('photoshop', '')
            talk('launching photoshop' + str(open_app()))

        if 'stop' in command:
                killing = command.replace('stop', '')
                talk("photoshop should be death now..." + str(close_app()))
        if  'show me my love pictures one' in command:
            song = command.replace('show me my love pictures one', '')
            img = Image.open(my_pics_list_()[0])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'show me my love pictures two' in command:
            song = command.replace('show me my love pictures two', '')
            img = Image.open(my_pics_list_()[1])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'show me my love pictures three' in command:
            song = command.replace('show me my love pictures three', '')
            img = Image.open(my_pics_list_()[2])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'show me my love pictures four' in command:
            song = command.replace('show me my love pictures four', '')
            img = Image.open(my_pics_list_()[3])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'show me my love pictures five' in command:
            song = command.replace('five', '')
            img = Image.open(my_pics_list_()[4])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'show me my love pictures six' in command:
            song = command.replace('show me my love pictures six', '')
            img = Image.open(my_pics_list_()[5])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'show me my love pictures seven' in command:
            song = command.replace('show me my love pictures seven', '')
            img = Image.open(my_pics_list_()[6])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'show me my love pictures eight' in command:
            song = command.replace('show me my love pictures eight', '')
            img = Image.open(my_pics_list_()[7])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'show me my love pictures nine' in command:
            song = command.replace('show me my love pictures nine', '')
            img = Image.open(my_pics_list_()[8])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures() 
        if  'show me my love pictures ten' in command:
            song = command.replace('show me my love pictures ten', '')
            img = Image.open(my_pics_list_()[9])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'show me my love pictures eleven' in command:
            song = command.replace('show me my love pictures eleven', '')
            img = Image.open(my_pics_list_()[10])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'show me my love pictures twilve' in command:
            song = command.replace('twilve', '')
            img = Image.open(my_pics_list_()[11])
            talk("opening" + str(img))
            img.show()
            sleep(1)
            close_pictures()
        if  'python' in command:
            song = command.replace('python', '')
            webbrowser.open(pdf_read()[1])
            talk("opening python" )
        if  'java' in command:
            song = command.replace('java', '')
            webbrowser.open(pdf_read()[0])
            talk("opening java" )
        continue