from flask import Flask, make_response, request

app = Flask(__name__)

# =====================================================================
# SKENARIO 2: Hardcoded Secret Key (Memicu Vulnerability - Blocker)
# Mengekspos kunci rahasia secara terang-terangan di dalam kode.
# Referensi: CWE-798
# =====================================================================
app.secret_key = "SuperSecretKey_Yang_Seharusnya_Disembunyikan_Di_ENV"

# =====================================================================
# SKENARIO 5: CSRF Protection Disabled (Memicu Security Hotspot)
# Mematikan proteksi dasar framework terhadap serangan pemalsuan request.
# Referensi: CWE-352
# =====================================================================
app.config['WTF_CSRF_ENABLED'] = False

@app.route('/')
def index():
    response = make_response("Sistem sedang diuji oleh Jenkins dan SonarQube!")
    
    # =====================================================================
    # SKENARIO 4: Cookie Misconfiguration (Memicu Security Hotspot)
    # Membuat session cookie sensitif namun tanpa atribut secure=True
    # Referensi: CWE-1004
    # =====================================================================
    response.set_cookie('session_id', 'user_token_12345', secure=False, httponly=False)
    
    return response

if __name__ == '__main__':
    # =====================================================================
    # SKENARIO 3: Debug Mode Active (Memicu Security Hotspot)
    # Menyalakan mode debug di lingkungan produksi secara eksplisit.
    # Referensi: CWE-489
    # =====================================================================
    app.run(host='0.0.0.0', port=5000, debug=True)
