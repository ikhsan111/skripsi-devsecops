from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/cari', methods=['GET'])
def cari():
    user_input = request.args.get('q', '')
    
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    # --- INI YANG DICARI SONARQUBE ---
    # Rule "Formatting SQL queries" mencari tanda tambah (+) di dalam string SQL
    # Ini dianggap Security-Sensitive
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    
    cursor.execute(query)
    
    return "Search Done"

if __name__ == '__main__':
    app.run(debug=True)
