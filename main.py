import connexion
from flask import Flask, render_template

# app = Flask(__name__, template_folder="templates")
app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/01')
def test_header():
    connexion.request.

if __name__ == '__main__':
    app.run(debug=True)
