from flask import Flask, session

app = Flask(__name__)

# ==========================================
# SKENARIO 2: HARDCODED SECRET KEY (CWE-798)
# ==========================================
# SonarQube akan langsung memblokir pipeline karena baris di bawah ini.
# Kunci rahasia ditulis langsung (hardcoded) di dalam source code.

app.secret_key = "R4h4s1a_N3g4rA_123!!" 

# Alternatif penulisan yang juga akan dideteksi oleh SonarQube:
# app.config['SECRET_KEY'] = "R4h4s1a_N3g4rA_123!!.
# ==========================================

@app.route('/')
def home():
    # Contoh penggunaan secret key untuk mengamankan session
    session['user'] = 'ikhsan_admin'
    return "Selamat datang! Session telah dibuat menggunakan Hardcoded Secret Key."

if __name__ == '__main__':
    # Mode debug=True juga biasanya menjadi temuan (Hotspot) di SonarQube
    app.run(host='0.0.0.0', port=5000, debug=True)