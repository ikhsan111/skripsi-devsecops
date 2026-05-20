from flask import Flask, Response

app = Flask(__name__)

@app.route('/set-cookie')
def set_insecure_cookie():
    response = Response("Cookie diset dengan tidak aman!")
    
    # --- SKENARIO KERENTANAN: CWE-614 (Insecure Cookie) ---
    # SonarQube akan mendeteksi baris ini karena:
    # 1. secure=False: Cookie dikirim via HTTP (rentan MitM)
    # 2. httponly=False: Cookie dapat dicuri oleh JavaScript (rentan XSS)
    response.set_cookie(
        'session_id', 
        'user_secret_12345', 
        secure=False, 
        httponly=False, 
        samesite=None
    )
    # -----------------------------------------------------
    
    return response

if __name__ == '__main__':
    app.run(debug=True)