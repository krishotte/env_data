import connexion
import json
from flask import Flask, render_template
import db


# app = Flask(__name__, template_folder="templates")
app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/users', methods=['GET', 'POST'])
def users():
    if connexion.request.method == 'GET':
        return json.dumps(db.read_users())

    if connexion.request.method == 'POST':
        # print(f'POST request headers: {connexion.request.headers}')
        token = connexion.request.headers.get("Token")
        data = json.loads(connexion.request.json)
        print(f'Token: {token}')
        print(f'JSON: {data}')

        if len(data["name"]) > 0:
            print('writing data to db')
            db.add_user(data['name'])
            return json.dumps({"result": True})  # render_template('home.html')

        else:
            print('not correct data')
            return json.dumps({'result': False})


@app.route('/demodata', methods=['POST'])
def demo_data():
    if connexion.request.method == 'POST':
        # print(f'POST request headers: {connexion.request.headers}')
        token = connexion.request.headers.get("Token")
        data = json.loads(connexion.request.json)
        print(f'Token: {token}')
        print(f'JSON: {data}')

        try:
            print('writing data to db')
            db.add_demo_data(
                battery=data["battery"],
                temperature=data["temperature"],
                humidity=data["humidity"]
            )
            return json.dumps({"result": True})  # render_template('home.html')

        except Exception:
            print('not correct data')
            return json.dumps({'result': False})


if __name__ == '__main__':
    app.run(debug=True)
