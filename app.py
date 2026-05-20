from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Simulasi kesalahan yang memicu error
    # Jika debug=True, stack trace akan muncul di browser
    return 1 / 0 

# --- SKENARIO KERENTANAN: CWE-200 (Exposure of Sensitive Information) ---
# Mengaktifkan 'debug=True' di lingkungan produksi adalah miskonfigurasi fatal.
# Hal ini melanggar prinsip keamanan dasar karena mengekspos detail sistem.
if __name__ == '__main__':
    app.run(debug=True) 
# ------------------------------------------------------------------------