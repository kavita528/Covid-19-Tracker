from flask import * 
from bs4 import BeautifulSoup 
import requests


page=requests.get("https://www.worldometers.info/coronavirus/country/india/")
soup=BeautifulSoup(page.content,'html.parser')
value=soup.find_all(class_="maincounter-number")
p=value[0].get_text()
p2=value[1].get_text()
p3=value[2].get_text()
print(p) 
app = Flask(__name__)  
 
@app.route('/')  
def message(): 
      return render_template('index.html',inf=[p,p2,p3])  
     
@app.route('/symptoms')  
def symptoms():  
      return render_template('symptoms.html')
@app.route('/advise')  
def advise():  
      return render_template('advise.html')
@app.route('/prevention')  
def prevention():  
      return render_template('prevention.html')
@app.route('/quiz')  
def quiz():  
      return render_template('quiz1.html')
if __name__ == '__main__':  
   app.run(debug = True)  