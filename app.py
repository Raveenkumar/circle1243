import os
from flask import Flask

app = Flask(__name__)


@app.route('/',methods= ['GET','POST'])
def index():
    return 'Flask app is running'
#port = int(os.getenv('PORT',5001)))

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)