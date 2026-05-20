from flask import Flask, session

app = Flask(__name__)

# --- SKENARIO KERENTANAN: CWE-614 (Insecure Cookie) ---
# Secara default, Flask session cookie mungkin tidak memiliki atribut 'Secure'.
# Jika dijalankan di lingkungan produksi tanpa konfigurasi yang benar, 
# cookie ini rentan terhadap serangan Man-in-the-Middle (MitM).
app.secret_key = 'kunci-rahasia-banget'
app.config.update(
    SESSION_COOKIE_HTTPONLY=False, # Rentan XSS
    SESSION_COOKIE_SECURE=False,   # Rentan intersepsi melalui HTTP
    SESSION_COOKIE_SAMESITE=None   # Rentan CSRF
)
# -----------------------------------------------------

@app.route('/')
def index():
    session['user'] = 'admin'
    return "Cookie sesi telah diset tanpa atribut keamanan."

if __name__ == '__main__':
    app.run(debug=True)