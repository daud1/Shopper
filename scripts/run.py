from flask import Flask
from forms import LoginForm
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from shopping_list import Item, ShoppingList

                        ###initialisation###
app = Flask('__name__', template_folder='../UI', static_folder='../UI')
app.config.from_object('settings')

                        ###views and auth###
@app.route('/', methods=['GET', 'POST'])
def index():
    err = None
    form = LoginForm()
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            err = 'Invalid Credentials, Try Again!'
        else:
           return redirect(url_for('lists'))
    return render_template('login.html', error=err, form=form)

@app.route('/lists')
def lists():
    return render_template('shoppinglistview.html')

                        ###run###
if __name__ == '__main__':
    app.run(debug=True)