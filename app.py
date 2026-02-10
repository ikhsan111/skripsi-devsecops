from flask import Flask, request, make_response
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    user_input = request.args.get('username', '')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # --- PENTING: KEMBALI KE METODE VARIABEL ---
    # SonarQube Community lebih mudah mendeteksi jika string SQL 
    # disimpan dalam variabel terpisah dulu, baru dieksekusi.
    
    # Kita gunakan .format() sesuai deskripsi rule yang Anda kirim:
    # "Formatted SQL queries can be difficult to maintain... and increase risk"
    sql_query = "SELECT * FROM users WHERE username = '{0}'".format(user_input)
    
    # Jalankan variabel tersebut
    cursor.execute(sql_query)
    
    data = cursor.fetchall()
    conn.close()

    # Bagian ini sudah OK (XSS/Cookie)
    response = make_response("Login Processed")
    response.set_cookie('session_id', 'rahasia12345')

    return response

if __name__ == '__main__':
    app.run(debug=True)
