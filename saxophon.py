import os
import sys
import time
from selenium import webdriver
from tkinter import *
from tkinter import filedialog, simpledialog, messagebox, Spinbox

def close():
    sys.exit()

varis = {
    "username" : "",
    "passwort" : "",
    "recipient" : "",
    "subject" : "",
    "text" : "",
    "loops" : ""
}

fileEnt = ""

def button_action():
    global varis
    mt = ""
    varis["username"] = usernameEnt.get()
    varis["passwort"] = passwortEnt.get()
    varis["recipient"] = recipientEnt.get()
    varis["subject"] = subjectEnt.get()
    varis["text"] = textEnt.get("1.0", END)
    varis["loops"] = loopNum.get()

    for x in varis:
        if (varis[x] == ""):
            mt = "true"
    if (mt == "true"):
        messagebox.showwarning(title="Achtung", message="Nicht alle Felder ausgefüllt, Programm kann nicht ausgeführt werden!")
    else:
        fenster.destroy()


def openfile():
    global varis
    fileEnt = filedialog.askopenfilename()
    filelabel.config(text="Datei geladen")

#baut GUI
fenster = Tk()
fenster.title("Lernsax-Spambot")
fenster.geometry('300x500')

Label(fenster, text="Username:").pack()
usernameEnt = Entry(fenster)
usernameEnt.pack()
Label(fenster, text="Passwort:").pack()
passwortEnt = Entry(fenster)
passwortEnt.pack()
Label(fenster, text="").pack()
Label(fenster, text="Empfänger:").pack()
recipientEnt = Entry(fenster)
recipientEnt.pack()
Label(fenster, text="Betreff:").pack()
subjectEnt = Entry(fenster)
subjectEnt.pack()
Label(fenster, text="Text:").pack()
frame=Frame(fenster, width=200, height=100)
frame.pack()
textEnt = Text(frame)
textEnt.place(x=0, y=0, height=100, width=200)
Label(fenster, text="Anzahl der Mails:").pack()
loopNum = Spinbox(fenster, from_=1, to=69420)
loopNum.pack()
Label(fenster, text="(Optional) Datei:").pack()
Button(fenster, text="Datei laden", command=openfile).pack()
filelabel = Label(fenster, text="")
filelabel.pack()

ok_btn = Button(fenster, text="Ok", command=button_action, padx=10)
ok_btn.pack(pady=10)
Button(fenster, text="Programm beenden", command=close).pack()
mainloop()

#setup - lädt die Orte für Browser und Eingabefenster
chromedriver_location = os.path.dirname(os.path.abspath(__file__))+'\chromedriver.exe'
chromedriver_location = chromedriver_location.replace('\\', '/')
driver = webdriver.Chrome(chromedriver_location)

username_field = '//*[@id="login_login"]'
passwort_field = '//*[@id="login_password"]'
loginButton = '//*[@id="a745761"]/input[4]'
email_link = '//*[@id="menu_105592"]'
upload = '//*[@id="main_content"]/table[5]/tbody/tr/td[3]/input'

#öffnet den mail-bereich von lernsax
driver.get('https://www.lernsax.de/wws/9.php#/wws/100001.php?sid=73686923944239016459925482550630S1adb4d16')
driver.switch_to.frame(driver.find_element_by_id('main_frame'))
driver.find_element_by_xpath(username_field).send_keys(varis["username"])
driver.find_element_by_xpath(passwort_field).send_keys(varis["passwort"])
driver.find_element_by_xpath(loginButton).click()
driver.find_element_by_link_text('E-Mail').click()

#verschickt mails
for i in range(int(varis["loops"])):
    driver.find_element_by_link_text('E-Mail schreiben').click()
    time.sleep(0.5)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_class_name('iframe_popup'))
    driver.find_element_by_id('to').send_keys(varis["recipient"])
    driver.find_element_by_id('subject').send_keys(varis["subject"])
    driver.find_element_by_id('body').send_keys(varis["text"])

    if (fileEnt != ''):
        driver.find_element_by_id('file').send_keys(fileEnt)
        element = driver.find_element_by_xpath(upload).click()

    driver.find_element_by_name('send_mail').click()
    driver.execute_script('return ww.close();')
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_id('main_frame'))