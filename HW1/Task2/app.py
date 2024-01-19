from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/category/<string:name>')
def category(name):
    return render_template('category.html', category_name=name)

@app.route('/product/<string:category>/<string:name>')
def product(category, name):
    return render_template('product.html', category_name=category, product_name=name)

if __name__ == '__main__':
    app.run(debug=True)
