from flask import Flask, request, make_response
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Input dari user
    user_input = request.args.get('username', '')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # --- JURUS PAMUNGKAS: EXEC() ---
    # Kita membungkus query SQL di dalam fungsi exec().
    # SonarQube SANGAT MEMBENCI fungsi exec().
    # Ini akan memicu rule: "Using 'exec' is security-sensitive"
    # atau "Dynamic code execution".
    
    # Teknik ini sering dipakai hacker, jadi ini sangat valid sebagai simulasi serangan.
    sql_payload = "cursor.execute(\"SELECT * FROM users WHERE username = '" + user_input + "'\")"
    exec(sql_payload)
    
    conn.close()

    # --- BAGIAN INI SUDAH SUKSES (XSS/COOKIE) ---
    response = make_response("Login Processed")
    response.set_cookie('session_id', 'rahasia12345')

    return response

if __name__ == '__main__':
    app.run(debug=True)
