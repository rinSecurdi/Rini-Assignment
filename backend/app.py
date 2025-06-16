from flask import Flask
import os
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    try:
        db = pymysql.connect(
            host='mysql',
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE']
        )
        db.close()
        return "Connected to MySQL successfully!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
