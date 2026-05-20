import hashlib
from flask import Flask, request

app = Flask(__name__)

# --- SKENARIO KERENTANAN: CWE-327 (Broken Cryptographic Algorithm) ---
def get_hash(data):
    # MD5 sudah usang (deprecated) dan tidak aman untuk keperluan keamanan
    # SonarQube akan mendeteksi ini sebagai "Security Hotspot"
    return hashlib.md5(data.encode()).hexdigest()
# ---------------------------------------------------------------------

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    hashed_password = get_hash(password)
    # Logika autentikasi...
    return f"Password di-hash dengan MD5: {hashed_password}"

if __name__ == '__main__':
    app.run(debug=True)