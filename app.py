from flask import Flask, session

app = Flask(__name__)

# Konfigurasi ini secara eksplisit melanggar standar keamanan
# SonarQube akan mendeteksi SESSION_COOKIE_SECURE=False sebagai Hotspot
app.config.update(
    SESSION_COOKIE_HTTPONLY=False, 
    SESSION_COOKIE_SECURE=False,   
    SESSION_COOKIE_SAMESITE=None   
)

# Endpoint ini akan memicu deteksi karena tidak ada proteksi token
@app.route('/transfer_funds', methods=['POST'])
def transfer():
    # Simulasi transaksi tanpa token CSRF
    # SonarQube akan mendeteksi bahwa ini adalah 'state-changing request'
    return "Dana berhasil ditransfer"

if __name__ == '__main__':
    app.run()