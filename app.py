from flask import Flask, request

app = Flask(__name__)

# --- SKENARIO KERENTANAN: CWE-352 (CSRF) ---
# SonarQube akan mendeteksi ini sebagai kerentanan karena melakukan 
# 'state-changing operation' tanpa validasi anti-CSRF token.
@app.route('/update-password', methods=['POST'])
def update_password():
    # Input dari user diambil langsung tanpa pengecekan token
    new_password = request.form.get('password')
    
    # Simulasi update ke database
    # Pada titik ini, aplikasi rentan terhadap serangan CSRF.
    # Penyerang bisa memaksa korban menekan link yang mengirim POST ke sini.
    return f"Password berhasil diubah menjadi: {new_password}"
# -------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)