from flask import Flask, redirect, render_template
from datetime import timedelta,datetime


#CREO L'APP E SETTO UNA SECRET KEY
app = Flask(__name__)
app.config['SECRET_KEY'] = 'TestFlaskAPI'
app.permanent_session_lifetime = timedelta(minutes=60)

@app.route('/',methods=['GET'])
def main():
    return redirect('/home')

#GESTIONE DELLE VIEWS
#IMPORT VIEW
from services.devices import DevicesView
#FINE IMPORT VIEW
DevicesView.register(app, route_prefix='/api/')

if __name__=="__main__":
    app.run(port=8081)


