import json

from flask import Flask, redirect, url_for, request, session, render_template
from flask_wtf.csrf import CSRFProtect
import random

from app.forms import LoginForm, RegistrationForm
import app.db as db


app = Flask(__name__)
app.config['SECRET_KEY'] = '351357346492509682309879678987568'
csrf = CSRFProtect(app)
db.init(app)


@app.route('/')
def index():
    if 'session_id' in session:
        return redirect(url_for('account'))
    else:
        return redirect(url_for('loginn'))


@app.route('/login/', methods=['GET', 'POST'])
def loginn():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # проверяем валидность
        email = form.email.data
        password = form.password.data
        user = db.get_user(email, password)
        if user:
            session['session_id'] = random.getrandbits(128)
            session['first_name'] = user.first_name
            session['second_name'] = user.second_name
            session['email'] = user.email
        else:
            render_template('login.html', title="Login", registerlink=url_for('register'), form=form, error="Пользователь с такими именем и логином не найден")
    if 'session_id' in session:
        return redirect(url_for('account'))
        #return render_template('personal_page.html', title="Account", logout_link=url_for('logout'), user=user)
    else:
        return render_template('login.html', title='Login', registerlink=url_for('register'), form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        usr_chk = db.user_exists(form.email.data)
        if usr_chk:
            #todo уже есть такой
            render_template('register.html', title='Register', loginlink=url_for('loginn'), form=form, error="Такой польщователь уже есть в системе.")
        else:
            db.add_user(form.email.data,
                        form.password.data,
                        form.first_name.data,
                        form.second_name.data)
            return redirect(url_for('loginn', message='Утпешно зарегистрирован в системе'))
        session['username'] = request.form.get('username') or 'MoName'
    return render_template('register.html', title='Register', loginlink=url_for('loginn'), form=form)

@app.route('/account/')
def account():
    user = {}
    user['first_name'] = session['first_name']
    user['second_name'] = session['second_name']
    user['email'] = session['email']
    return render_template('personal_page.html', user=user, logoutlink=url_for('logout'))

@app.route('/logout/')
def logout():
    session.pop('session_id', None)
    return redirect(url_for('loginn'))


@app.cli.command("install")
def install():
    db.install()
    print('DB install done!')


if __name__ == '__main__':
    app.run(debug=True)



