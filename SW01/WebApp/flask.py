from flask import Flask,redirect,request,url_for,render_template
import requests
app=Flask(__name__)
# @app.route('/hello/<name>')
# def hello(name):
#     return f'Hello {name}'

# @app.route('/result',methods=['POST','GET'])
# def result():
#     if(request.method=='POST'):
#         dict={'name':'Aryan','class':'2nd year'}
#         #dict=request.form
#         return render_template('result.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        n = request.form['usn']
        res=requests.get('http://codeforces.com/api/user.info?handles='+n)
        sub=requests.get('http://codeforces.com/api/user.status?handle='+n+'&from=1&count=1')
        dict=res.json()
        dict2=sub.json()
        dict3={}
        dict3={'fname':dict['result'][0]['firstName'],'lname':dict['result'][0]['lastName'],'rating':dict['result'][0]['rating'],'location':dict['result'][0]['city'],'country':dict['result'][0]['country'],'college':dict['result'][0]['organization'],'rank':dict['result'][0]['rank'],'maxrating':dict['result'][0]['maxRating'],'maxrank':dict['result'][0]['maxRank'],'url':"https:"+dict['result'][0]['titlePhoto']}

        return render_template('result.html',ans=dict3)
@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.debug=True
    app.run()
