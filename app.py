from flask import Flask, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "kunci_rahasia_untuk_session"

# Menginisialisasi pelindung CSRF untuk seluruh aplikasi
csrf = CSRFProtect(app)

@app.route('/')
def home():
    return "Selamat datang di Aplikasi Web. Sistem CSRF sedang diuji."

# =====================================================================
# SKENARIO 5: PENGUJIAN CSRF DISABLED / EXEMPTED
# Mengecualikan rute yang mengubah data (POST) dari perlindungan CSRF.
# Ini adalah Bad Practice (CWE-352) yang pasti ditangkap SonarQube.
# =====================================================================
@app.route('/transfer_dana', methods=['POST'])
@csrf.exempt  # <--- DEKORATOR INI ADALAH PENYEBAB KERENTANAN
def transfer_dana():
    rekening_tujuan = request.form.get('rekening')
    jumlah = request.form.get('jumlah')
    
    # Bahaya: Karena ada @csrf.exempt, penyerang bisa membuat web palsu 
    # yang memaksa browser korban mengirim request POST ke URL ini 
    # tanpa perlu token validasi.
    
    return f"Berhasil mentransfer Rp {jumlah} ke rekening {rekening_tujuan}!"

if __name__ == '__main__':
    app.run(debug=False)
