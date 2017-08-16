from flask import Flask
from flask import render_template

#------------------------------------------initialise the flask object------------------------
app = Flask('__name__', template_folder='UI', static_folder='UI')

#-----------------------views------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/lists')
def lists():
    return render_template('shoppinglistview.html')

#--------------------------------run the app---------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
