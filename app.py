from flask import Flask,request,render_template         
from bs4 import BeautifulSoup
import requests, time, smtplib        
from datetime import datetime
import re                  
import requests as r                  
from bs4 import BeautifulSoup as bs
app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def home():
    	if request.method == 'POST':
    	  medicine_name= request.form.get('medicine_name')
    	  link="https://www.1mg.com/search/all?filter=true&name="+medicine_name
    	  html_page = r.get(link)
    	  soup = BeautifulSoup(html_page.content,"html.parser")
    	  for i in soup.find_all('div',{'class':['style__horizontal-card___1Zwmt','style__product-box___3oEU6']}):
    	    link = i.find('a',href=True)
    	    if link is None:
    	        continue
    	    link1 = link['href']
    	    break
    	  else:
    	    link1="N/A"
    	  if link1=="N/A":
    	    price="N/A"
    	  else:
    	    quantity=soup.find("div" , {"class": "style__pack-size___3jScl"}).text
    	    title=soup.find("div" , {"class": "style__pro-title___3G3rr"}).text
    	    stock=soup.find("div" , {"class": "style__interaction___3cb12"}).text
    	    if stock=="ADD":
    	      a="available"
    	    else:
    	      a="N/A"
    	    print(a)
    	    url1= "https://www.1mg.com" +link1
    	    page1 = r.get(url1)
    	    soup = bs(page1.content, "html.parser")
    	    price=soup.find("span" , {"class": "l3Regular"}).text
    	    price = price[1:]
    	  url2= "https://pharmeasy.in/search/all?name="+medicine_name
    	  p=r.get(url2)
    	  soup = BeautifulSoup(p.text, 'html.parser')
    	  for i in soup.find_all("div" ,{"class":"GvJNB"}):
    	    link = i.find('a',href=True)
    	    if link is None:
    	        continue
    	    link2=link['href']
    	    print(link2)
    	    break
    	  else:
    	    link2="N/A"
    	  if link2=="N/A":
    	    print("N/A")
    	  else:
    	    url3="https://pharmeasy.in"+link2
    	    s=r.get(url3)
    	    soup1 = BeautifulSoup(s.text, 'html.parser')
    	    price1=soup1.find("div" ,{"class":"_1_yM9"}).text
    	    print(price1)
    	    title1= soup.find('h1',{'class':'ooufh'}).text
    	    print(title1)
    	    quantity1= soup.find('div',{'class':'_36aef'}).text
    	    print(quantity1)
    	    for i in soup1.find('div',{'class':'_3bwoY'}):
    	      link = i.find('button',{'class':'_2FE4Z h1H8I _1JBjj notifyMeBtn'})
    	      if link is None:
    	          continue
    	      link2=link.text
    	      print(link2)
    	      break
    	    else:
    	      link2="N/A"
    	    if link2=="Notify Me":
    	      stock=" not availble"
    	    else:
    	      stock="availble"
    	    print(stock)
    	    link3="https://www.practo.com/medicine-info/search?drug="+medicine_name
    	    s = r.get(link3)
    	    soup = BeautifulSoup(s.content,'html.parser')
    	    for i in soup.find_all("div" , {"class":"shdzcg-1 cjDIVa"}):
    	      link = i.find('a',href=True)
    	      if link is None:
    	         continue
    	      link4 = link['href']
    	      print(link4)
    	      break
    	    else:
    	      link1="N/A"
    	    if link1=="N/A":
    	      print("N/A")
    	    else:
    	      quantity3=soup.find("div", {"class":"s4h2ti-3 RQtd"}).text
    	      print(quantity3)
    	      price3=soup.find("div" , {"class": "s13j2pak-2 hfenSr"}).text
    	      print(price3)
    	      for i in soup.find('div',{'class':'shdzcg-1 cjDIVa'}):
    	        stock2=i.find('span',{'class':'s10ai0bh-0 cDKUIr'})
    	        if stock2 is None:
    	            continue
    	        stock2=stock2.text
    	        if stock2=="Add to cart":
    	          p="available"
    	        else:
    	          p="N/A"
    	        print(p)
    	        link="https://www.practo.com"+str(link4)
    	        html_page = r.get(link)
    	        soup = BeautifulSoup(html_page.content,"lxml")
    	        title3= soup.find("div", {"class":"product-info__section"}).text
    	        print(p)
    	      link3="https://www.zoylo.com/medicines/catalogsearch/result/?q="+medicine_name
    	      html_page = r.get(link3)
    	      soup = BeautifulSoup(html_page.content,"lxml")
    	      for i in soup.find_all("div" ,{"class":"product details product-item-details"}):
    	        link = i.find('a',href=True)
    	        if link is None:
    	            continue
    	        link5=link['href']
    	        print(link5)
    	        break
    	      else:
    	        link5="N/A"
    	      if link5=="N/A":
    	        print("N/A")
    	      else:
    	        price4=soup.find("span" , {"class": "price"}).text
    	        print(price4)
    	        html_page = r.get(link2)
    	        soup = bs(html_page.content,"lxml")
    	        for i in soup.find_all("div" ,{"class":"col-md-12 section-three"}):
    	          link=i.find("button" ,{"class":"action primary tocart"})
    	          if link is None:
    	              continue
    	          link=link.text
    	          link=link[1:2]
    	          print(link)
    	          break
    	          if link=='A':
    	            stock3="Medicine_available"
    	          else:
    	            stock3="not_available"
    	        quantity4=soup.find("div" ,{"class":"col-lg-8 pack-size"}).text
    	        print(quantity4)
    	      return render_template("index.html",price=price,url1=url1,title=title,quantity=quantity,stock=stock,link2=link2,title1=title1,a=a,url3=url3,title3=title3,price3=price3,quantity3=quantity3,p=p,link=link,quantity4=quantity4,price4=price4,stock3=stock3,link5=link5)
    	    return render_template("index.html")
if __name__ == '__main__':
	app.run(debug=True)
	app.run()
