import os
from flask import Flask, render_template, flash, redirect, request, url_for
from datetime import date
now = date.today()
now=str(now)
from flask_mysqldb import MySQL
import requests
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

app = Flask(__name__)
app.secret_key = 'gryg56hjfejjffd7i'                    
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'XuQfP6V8WJ'
app.config['MYSQL_PASSWORD'] = 'uYEVTADtgZ'
app.config['MYSQL_DB'] = 'XuQfP6V8WJ'                   
mysql = MySQL(app)
@app.route('/')
@app.route('/get_tasks')
def get_tasks():
  cur = mysql.connection.cursor()
  cur.execute("SELECT * FROM Class")
  tasks_table=cur.fetchall()
  return render_template("tasks.html", Class=tasks_table)
@app.route('/add_task')
def add_task():
  cur = mysql.connection.cursor()
  cur.execute("SELECT * FROM Class")
  tasks_table = cur.fetchall()
  return render_template("addtask.html",Class=tasks_table)
@app.route("/edit_taskk", methods=['GET','POST'])
def edit_taskk():
  url= request.form.get('task_name')
  cur = mysql.connection.cursor()
  cur.execute("SELECT * FROM Class")
  t = cur.fetchall()
  ca=request.form['category']
  print(ca)
  chrome_options = Options()
  options = Options()
  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--no-sandbox")
  driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
  gmail_id="aman765180@gmail.com"
  gmail_name="attendance"
  gmail_pass="Njjhhj"
  attend=None
  driver.get(url)
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="smartJoinButton"]').click()
  time.sleep(2)
  driver.switch_to.frame("iframe_new_web_header")
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
    attend=my_tag.text
    lst+=attend
  print(lst)
  cur.execute("SELECT sroll FROM Class where Class_name=%s",[ca])
  l=cur.fetchone()
  l=l[0]
  res = str(l)[3:-5] 
  print(res)
  ll=int(l)
  cur.execute("SELECT eroll FROM Class where Class_name=%s",[ca])
  u=cur.fetchone()
  u=u[0]
  res1 = str(u)[3:-5]
  uu=int(u)
  print(uu)
  pr="present"
  aa="Absent"
  num=""
  for num in range(ll, uu + 1):
    nums=str(num)
    if nums in lst:
      cur.execute("INSERT INTO Attendence (Class_name,Rollno , Attendence,date) VALUES (%s, %s, %s,%s)", (ca, nums, pr,now))
      print(nums,'present')
    else:
      cur.execute("INSERT INTO Attendence (Class_name, Rollno, Attendence,date) VALUES (%s, %s, %s,%s)", (ca,nums, aa,now))
      mysql.connection.commit()
      print(nums,'absent')
    #return render_template('edittask.html', Class=t)
    
  return redirect(url_for('get_tasks'))
#@app.route('/showw')
#def result():
 # RollNo=request.form.get('RollNo')
 # print(RollNo)
  #cl=request.form.get('task_name1')
  #cur = mysql.connection.cursor()
  #cur = mysql.connection.cursor()
  #cur.execute("SELECT * FROM Attendence where (RollNo=%s AND Class_Name=%s)",(RollNo,cl))
  #mysql.connection.commit()
  #tt=cur.fetchall()
  #return render_template('attend.html')
  
@app.route('/res', methods=['GET','POST'])
def res():
  a="present"
  RollNo=request.form.get('RollNo')
  print(RollNo)
  cl=request.form.get('task_name1')
  cur = mysql.connection.cursor()
  cur.execute("SELECT * FROM Attendence where (RollNo=%s AND Class_Name=%s)",(RollNo,cl))
  tt=cur.fetchall()
  total=cur.execute("SELECT COUNT(*) FROM Attendence  WHERE (Rollno=%s AND Class_name=%s)",(RollNo,cl))
  total=cur.fetchone()
  p=cur.execute("SELECT COUNT(*) FROM Attendence WHERE (Attendence=%s AND Rollno=%s AND Class_name=%s)",(a,RollNo,cl))
  p=cur.fetchone()
  q=p[0]
  q=int(q)
  print(q)
  t=total[0]
  t=int(t)
  print(t)
  if t==0:
    per=0
  else:
    per=q*100/t
  print(per)
  #mysql.connection.commit()
  #tt=cur.fetchall()
  return render_template("attend.html",det=tt,per=per,q=q,t=t)
  #return redirect(url_for('showw'))                 
@app.route('/edit_task')
def edit_task():
  cur = mysql.connection.cursor()
  cur.execute("SELECT * FROM Class")
  t = cur.fetchall()
  return render_template('edittask.html', Class=t)
@app.route('/insert_task', methods=['POST'])
def insert_task():
  title=request.form.get('task_namee')
  print(title)
  rl=request.form.get('task_name1')
  rl1=request.form.get('task_name2')
  cur = mysql.connection.cursor()
  cur.execute("INSERT INTO Class(Class_name,sroll,eroll) VALUES(%s,%s,%s)", [title,rl,rl1])
  mysql.connection.commit()
  return redirect(url_for('get_tasks'))                 
if __name__ == '__main__':
  app.run(debug=True)
