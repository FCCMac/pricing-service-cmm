from flask import Flask
from common.database import Database
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint
from models.alert import Alert
from models.store import Store
import random
import string
import os
from flask.templating import render_template

app = Flask(__name__)
app.secret_key = ''.join(random.choices(
    string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)

Database.initialize()


@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(store_blueprint, url_prefix='/stores')
app.register_blueprint(user_blueprint, url_prefix='/users')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
