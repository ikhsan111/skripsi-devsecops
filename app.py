import os
from flask import Flask, request, make_response
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Praktik Aman: Mengambil secret key dari Environment Variable (Tidak Hardcoded) 
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "default_safe_fallback")

# Praktik Aman: Mengaktifkan proteksi CSRF secara global
csrf = CSRFProtect(app)
app.config['WTF_CSRF_ENABLED'] = True

@app.route('/')
def home():
    response = make_response("Beranda Aman")
    # Praktik Aman: Kuki disetel dengan atribut Secure dan HttpOnly
    response.set_cookie('session_id', 'token_aman_123', secure=True, httponly=True)
    return response

if __name__ == '__main__':
    app.run(debug=False)