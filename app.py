from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- SKENARIO KERENTANAN: CWE-352 (CSRF) ---
# Endpoint ini menerima request POST tanpa pengecekan CSRF token.
# Penyerang dapat membuat formulir berbahaya di situs lain yang mengirim
# request ke endpoint ini untuk mengubah data pengguna.

@app.route('/update_profile', methods=['POST'])
def update_profile():
    # Simulasi perubahan data sensitif tanpa validasi CSRF token
    new_email = request.form.get('email')
    return f"Email berhasil diubah menjadi: {new_email}"
# -------------------------------------------

@app.route('/')
def index():
    # Form rentan karena tidak ada CSRF token
    return render_template_string('''
        <form action="/update_profile" method="POST">
            <input type="email" name="email">
            <button type="submit">Update Email</button>
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)