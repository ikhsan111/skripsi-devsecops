import os
from flask import Flask, make_response

app = Flask(__name__)

# =====================================================================
# SKENARIO 1: BASELINE (KODE AMAN)
# 1. Kunci rahasia dipanggil via Environment Variable (Tidak Hardcoded)
# 2. CSRF Protection tetap aktif (default)
# =====================================================================
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

@app.route('/')
def index():
    response = make_response("Sistem Berjalan dengan Aman di Lingkungan Produksi!")
    
    # 3. Cookie diset dengan atribut keamanan penuh (Secure & HttpOnly)
    response.set_cookie('session_id', 'user_token_12345', secure=True, httponly=True)
    return response

if __name__ == '__main__':
    # 4. Mode Debug Dimatikan
    app.run(host='0.0.0.0', port=5000, debug=False)
