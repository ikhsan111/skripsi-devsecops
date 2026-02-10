from flask import Flask, request, make_response
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    user_input = request.args.get('username', '')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = '" + user_input + "'")
    
    data = cursor.fetchall()
    conn.close()

    response = make_response("Login Processed")
    response.set_cookie('session_id', 'rahasia12345')

    return response

if __name__ == '__main__':
    app.run(debug=True)
