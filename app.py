from flask import Flask
from flask_wtf.csrf import CSRFProtect, csrf

app = Flask(__name__)

# 1. PELANGGARAN GLOBAL:
# Menonaktifkan CSRF secara global melalui konfigurasi aplikasi
app.config['WTF_CSRF_ENABLED'] = False 

csrf = CSRFProtect()
csrf.init_app(app)

# 2. PELANGGARAN PADA VIEW:
# Menggunakan @csrf.exempt secara eksplisit menonaktifkan proteksi pada endpoint ini
@app.route('/transfer', methods=['POST'])
@csrf.exempt  # SENSITIF: Ini akan langsung memicu rule SonarQube
def transfer_money():
    return "Dana telah ditransfer tanpa proteksi CSRF."

if __name__ == '__main__':
    app.run(debug=True)