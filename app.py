from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import shutil, os
from selenium import webdriver
import os
from PIL import Image
import time
from PIL import Image 
import schedule
import sys
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  options = FirefoxOptions()
  options.add_argument('--no-sandbox')
  options.add_argument("--headless")
  web = webdriver.Firefox(options=options, executable_path=os.environ.get("GECKODRIVER_PATH"),firefox_binary=os.environ.get("FIREFOX_BIN"))
  web.maximize_window()
  web.get("https://web.whatsapp.com/")
  web.implicitly_wait(50)
  web.save_screenshot("image.png")
  image = Image.open("image.png") 
  files=['image.png']
  web.quit()
  for f in files:
    shutil.copy(f, 'static')
  return render_template('home.html')
if __name__ == '__main__':
  app.run(debug=True)
  app.run()
