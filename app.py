from flask import Flask, render_template, request
import json
import re
import requests
from bs4 import BeautifulSoup
from models.item import Item
from common.database import Database
from models.alert import Alert

app = Flask(__name__)
Database.initialize()


@app.route('/', methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        url = request.form('url')
        tag_name = request.form('tag_name')
        query = json.loads(request.form('query'))
        Item(url, tag_name, query).save_to_mongo() 
      
    return render_template('new_item.html')
        


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
