import sqlite3
from flask import Flask, request

app = Flask(__name__)

# --- SKENARIO KERENTANAN: CWE-89 (SQL Injection) ---
# SonarQube akan langsung memblokir ini sebagai VULNERABILITY, bukan HOTSPOT.
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # KODE RENTAN: Menggunakan format string langsung ke query SQL
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query) 
    
    return "User ditemukan"
# ---------------------------------------------------

if __name__ == '__main__':
    app.run()