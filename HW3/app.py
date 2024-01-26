import db
from flask import Flask, render_template, flash
from form import RegistrationForm
from werkzeug.security import generate_password_hash



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mail1234'

 

@app.route('/', methods=['POST', 'GET'])  
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)

        if db.insert_user(form.first_name.data, form.last_name.data, form.email.data, hashed_password):
            
            flash('Регистрация прошла успешно!', 'success')
            return render_template('index.html', form=form)
        else:
            flash('Ошибка: Пользователь с таким email уже существует', 'danger')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    db.init_db()
    app.run(debug=True)