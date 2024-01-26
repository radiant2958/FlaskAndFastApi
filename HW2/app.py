from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST'])
def setcookie():
    user_name = request.form['name']
    user_email = request.form['email']

    resp = make_response(redirect('/welcome'))
    resp.set_cookie('userName', user_name)
    resp.set_cookie('userEmail', user_email)

    return resp

@app.route('/welcome')
def welcome():
    name = request.cookies.get('userName')
    if not name:
        return redirect('/')
    return render_template('welcome.html', name=name)

@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('userName')
    resp.delete_cookie('userEmail')
    return resp

if __name__ == '__main__':
    app.run(debug=True)

