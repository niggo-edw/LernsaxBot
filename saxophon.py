import os
import sys
import time
from selenium import webdriver

#setup - lädt die Orte für Browser und Eingabefenster
chromedriver_location = os.path.dirname(os.path.abspath(__file__))+'\chromedriver.exe'
chromedriver_location = chromedriver_location.replace('\\', '/')
driver = webdriver.Chrome(chromedriver_location)

username_field = '//*[@id="login_login"]'
username = 'niklas.werner@lghe.lernsax.de'
passwort_field = '//*[@id="login_password"]'
passwort = 'D131/2LdKBL'
loginButton = '//*[@id="a745761"]/input[4]'
email_link = '//*[@id="menu_105592"]'
upload = '//*[@id="main_content"]/table[5]/tbody/tr/td[3]/input'

recipient = 'anselm.noetzold@lghe.lernsax.de'
subject = 'aber gerne doch'
text = 'ich kann jetzt auch dateien anhängen. gib mir einfach ne zahl, nen betreff, nen text und optional noch n bild oder so, dann wird der herr professor vollgespamt'

sendFile = 'true'

#öffnet den mail-bereich von lernsax
driver.get('https://www.lernsax.de/wws/9.php#/wws/100001.php?sid=73686923944239016459925482550630S1adb4d16')
driver.switch_to.frame(driver.find_element_by_id('main_frame'))
driver.find_element_by_xpath(username_field).send_keys(username)
driver.find_element_by_xpath(passwort_field).send_keys(passwort)
driver.find_element_by_xpath(loginButton).click()
driver.find_element_by_link_text('E-Mail').click()

#verschickt mails
for i in range(3):
    driver.find_element_by_link_text('E-Mail schreiben').click()
    time.sleep(0.1)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_class_name('iframe_popup'))
    driver.find_element_by_id('to').send_keys(recipient)
    driver.find_element_by_id('subject').send_keys(subject)
    driver.find_element_by_id('body').send_keys(text + str(i))

    if (sendFile == 'true'):
        fileloc = 'C:/Users/Anwender/Documents/06 Programming/09lernsax-bot/foto.jpg'
        driver.find_element_by_id('file').send_keys(fileloc)
        element = driver.find_element_by_xpath(upload).click()

    driver.find_element_by_name('send_mail').click()
    driver.execute_script('return ww.close();')
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_id('main_frame'))