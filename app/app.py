from flask import Flask, render_template
import mysql.connector
import time

app = Flask(__name__)

def get_db_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host='db',
                user='root',
                password='group17',
                database='shop_db',
                charset='utf8mb4'
            )
            return conn
        except:
            time.sleep(2)

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', products=products)
    except Exception as e:
        return f"Lỗi kết nối Database: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)