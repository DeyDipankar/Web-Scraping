from flask import Flask,render_template,request
from autoscraper import AutoScraper

app = Flask(__name__)



@app.route('/',methods = ['GET','POST'])
def home():
    return render_template('scraper.html')

@app.route('/result',methods = ['GET','POST'])
def final_result():
    new_scraper = AutoScraper()
    new_url = request.form.get('field2',False)
    print(new_url)
    new_scraper.load('title&prices')
    result = new_scraper.get_result_similar(url=new_url,group_by_alias=True)
    return render_template('scraper.html',data = result)

if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)
    