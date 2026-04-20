from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response("Menguji Skenario 3 dan 4 untuk Skripsi")
    
    # =====================================================================
    # SKENARIO 4: Pembuatan Cookie Tanpa Secure Flag
    # =====================================================================
    response.set_cookie('sesi_login', 'rahasia123', secure=False, httponly=False)
    
    return response

if __name__ == '__main__':
    # =====================================================================
    # SKENARIO 3: Mengaktifkan Mode Debug
    # =====================================================================
    app.run(host='0.0.0.0', port=5000, debug=True)
