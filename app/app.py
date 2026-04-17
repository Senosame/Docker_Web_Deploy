from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__)
app.secret_key = 'group17'
 
# Cấu hình kết nối MySQL với charset UTF-8
db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'group17',
    'database': 'shop_db',
    'charset': 'utf8mb4',          # ← Fix lỗi chữ tiếng Việt
    'collation': 'utf8mb4_unicode_ci',
    'use_unicode': True,
}
 
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    conn.set_charset_collation('utf8mb4', 'utf8mb4_unicode_ci')
    return conn
 
@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', products=products, user=session.get('username'))
    except Exception as e:
        print(f"Lỗi kết nối DB: {e}")
        return render_template('index.html', products=[], error="Không thể kết nối cơ sở dữ liệu")
 
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = generate_password_hash(data['password'])
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (data['username'], hashed_pw)
        )
        conn.commit()
        return jsonify({"status": "success", "message": "Đăng ký thành công!"})
    except Exception as e:
        print(f"Register error: {e}")
        return jsonify({"status": "error", "message": "Tên đăng nhập đã tồn tại!"})
    finally:
        cursor.close()
        conn.close()
 
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (data['username'],))
        user = cursor.fetchone()
 
        if user and check_password_hash(user['password'], data['password']):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return jsonify({"status": "success", "username": user['username']})
 
        return jsonify({"status": "error", "message": "Sai tài khoản hoặc mật khẩu!"})
    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({"status": "error", "message": "Lỗi server!"})
    finally:
        cursor.close()
        conn.close()
 
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
 
@app.route('/checkout', methods=['POST'])
def checkout():
    if 'user_id' not in session:
        return jsonify({"status": "error", "message": "Vui lòng đăng nhập để thanh toán!"})
 
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO orders (user_id, total_price, items_json) VALUES (%s, %s, %s)",
            (session['user_id'], data['total'], str(data['items']))
        )
        conn.commit()
        return jsonify({"status": "success", "message": "Đơn hàng đã được lưu vào Database!"})
    except Exception as e:
        print(f"Checkout error: {e}")
        return jsonify({"status": "error", "message": "Lỗi khi lưu đơn hàng!"})
    finally:
        cursor.close()
        conn.close()
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)