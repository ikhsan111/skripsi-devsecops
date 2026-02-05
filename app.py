from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # --- CELAH KEAMANAN (VULNERABILITY) ---
    # Menggabungkan string secara langsung memicu SQL Injection.
    # SonarQube HARUS mendeteksi ini sebagai "Critical".
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(query) 
    return "Login Check Done"

if __name__ == '__main__':
    app.run(debug=True)
