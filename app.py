from flask import Flask, request

app = Flask(__name__)

# --- SKENARIO KERENTANAN: CWE-352 (CSRF) ---
# Aplikasi ini melakukan aksi sensitif (mengubah email) 
# melalui POST request tanpa validasi token CSRF.
@app.route('/change-email', methods=['POST'])
def change_email():
    new_email = request.form.get('email')
    # Simulasi pembaruan database
    # Tanpa CSRF token, penyerang bisa membuat form di situs lain 
    # yang mengirimkan request ke sini saat pengguna login.
    return f"Email berhasil diperbarui ke: {new_email}"
# -------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)