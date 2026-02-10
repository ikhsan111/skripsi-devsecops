from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    # Ambil input dari user
    user_input = request.args.get('q', '')

    # --- PANCINGAN 1: XSS (Cross-Site Scripting) ---
    # render_template_string dengan input mentah adalah XSS paling nyata.
    # SonarQube Community biasanya LANGSUNG mendeteksi ini sebagai "Vulnerability".
    # Rule: "Reflected XSS"
    xss_result = render_template_string("<h1>Hasil: " + user_input + "</h1>")

    # --- PANCINGAN 2: SQL Injection ---
    # Kita gunakan pola yang ditangkap oleh rule "Formatting SQL queries"
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    # Penggabungan string (+) pada query
    query = "SELECT * FROM data WHERE nama = '" + user_input + "'"
    cursor.execute(query) 
    
    return xss_result

if __name__ == '__main__':
    # Debug=True juga akan memicu Security Hotspot
    app.run(debug=True, port=5000)
