#!/usr/bin/env python


import os

from flask import Flask
from flask import request
from flask import make_response
import requests
import logging


# Flask app should start in global layout
app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)




@app.route('/webhook', methods=['GET'])
def webhook():
    response = requests.get('http://www.google.com')
    return response.text


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
