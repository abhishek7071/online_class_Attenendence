from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#import os
#driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
from PIL import Image
import time
from PIL import Image 
import sys
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import time
from PIL import Image 
import os
import smtplib
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def index():
  if request.method == 'POST':
    url= request.form.get('medicine_name')
    send= request.form.get('medicine_namee')
    chrome_options = Options()
    options = Options()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    gmail_id="aman765180@gmail.com"
    gmail_name="attendance"
    gmail_pass="Neesu@7071"
    attend=None
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="smartJoinButton"]').click()
    time.sleep(2)
    driver.switch_to.frame("pbui_iframe")
    driver.find_element_by_xpath('//input[@type="text"]').send_keys(gmail_name)
    driver.find_element_by_xpath("//input[@placeholder='Email address']").send_keys(gmail_id)
    driver.find_element_by_xpath("//button[@title='Next']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[@title='Got it']").click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="interstitial_join_btn"]').click()
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html)
    lst=""
    for my_tag in soup.find_all(class_="styles-user-name-gpTpQ"):
      #print(my_tag.text)
      attend=my_tag.text
      lst+=attend
      
    f= open("a.txt","w+")
    f.write(lst)
    driver.save_screenshot("image.png")
    #web.maximize_window()
    img_data = open('image.png','rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'aman765180@gmail.com'
    msg['To'] = send
    filename = "a.txt"
    f = open(filename)
    attachment = MIMEText(f.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(attachment)
    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data,'png')
    msg.attach(image)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('aman765180@gmail.com', 'Neesu@12345')
    s.sendmail('aman765180@gmail.com',send,msg.as_string())
    s.quit()
    return render_template('home.html',title=lst)
  return render_template("home.html")
if __name__ == '__main__':
  app.run(debug=True)
  app.run()
