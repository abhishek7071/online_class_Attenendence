from flask import Flask,request,render_template
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(
	    executable_path=os.environ.get("CHROMEDRIVER_PATH"),
	    chrome_options=chrome_options)
	driver.get("https://www.netmeds.com/catalogsearch/result/?q=Combiflam")
	elm = driver.find_element_by_tag_name('html')
	page_source = driver.page_source
	driver.quit()
	soup = bs(page_source, 'html.parser')
	divs = soup.find_all("div", attrs={'class': 'drug_list'})
	imgs = []
	names = []
	links = []
	for d in divs:
		img = d.find("img")
		img = img['src']
		drug = d.find("div", attrs={'class': 'drug_c'})
		drug = drug.find("a")
		link = 'https://www.netmeds.com'
		link += drug['href']
		return render_template("index.html",price=link)
	return render_template("index.html")
