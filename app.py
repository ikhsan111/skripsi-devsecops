from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/cari', methods=['GET'])
def cari():
    # INPUT USER (Sumber Masalah)
    keyword = request.args.get('q', '')

    # --- BUKTI 1: SQL INJECTION ---
    # Batasan Masalah: Mendeteksi SQL Injection
    # SonarQube akan mendeteksi ini sebagai "Formatting SQL queries is security-sensitive" (Hotspot)
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    # Penggabungan string (+) adalah ciri utama SQL Injection
    query = "SELECT * FROM produk WHERE nama = '" + keyword + "'"
    cursor.execute(query) 

    # --- BUKTI 2: XSS (Cross-Site Scripting) ---
    # Batasan Masalah: Mendeteksi XSS
    # SonarQube akan mendeteksi ini sebagai "Reflected XSS" atau Hotspot terkait Output
    # Menampilkan input mentah ke browser tanpa filter
    return render_template_string("<h1>Hasil Pencarian: " + keyword + "</h1>")

if __name__ == '__main__':
    app.run(debug=True)
