import os
from flask import Flask, session

app = Flask(__name__)

# ==========================================
# SKENARIO 1: BASELINE (KODE AMAN)
# ==========================================
# Kunci diambil dari Environment Variable server/Docker.
# Jika tidak ada, sistem akan error, tapi kode tetap aman karena 
# kunci rahasia tidak pernah ditulis di dalam file ini.

app.secret_key = os.environ.get('FLASK_SECRET_KEY')

# ==========================================

@app.route('/')
def home():
    session['user'] = 'ikhsan_admin'
    return "Selamat datang! Aplikasi berjalan aman."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)