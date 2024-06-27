from flask import Flask,render_template, request
import requests
app = Flask(__name__)

def get_weather_data(city):
    API_KEY='62c454ef720f1084b5aa45a724ce4d7a'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid={API_KEY}'
    r= requests.get(url).json()
    return r



@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='POST':
        ciudad=str(request.form.get('txtciudad'))
        data=get_weather_data(ciudad)
        
        return render_template('index.html',context=data)
    else:
     return render_template('index.html')
        
@app.route("/cv")
def curriculum():
    return render_template('hv.html')

@app.route("/login", methods=['GET','POST'])
def login():
     if request.method=='POST':
        USUARIO='ADMIN@GMAIL.COM'
        PASSWORD='ADMIN'
        user= request.form.get("txtEmail")
        password= request.form.get("txtPassword")
        if USUARIO == user and PASSWORD == password:
            return render_template('index.html')
        else:
            return render_template('login.html', error=True)
     return render_template ('login.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'),404

@app.route("/registro", methods=['GET','POST'])
def registro():
    return render_template('registro.html')

if __name__=='__main__':
    app.run(debug=True)
    
    