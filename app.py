from flask import Flask
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    # =====================================================================
    # SKENARIO 3 (BARU): Security Misconfiguration (Weak Cryptography)
    # Mengonfigurasi sistem untuk menggunakan algoritma MD5 yang sudah usang.
    # Ini PASTI akan memicu alarm Security Hotspot dari SonarQube.
    # =====================================================================
    data_rahasia = "password_pengguna_123"
    konfigurasi_hash_lemah = hashlib.md5(data_rahasia.encode()).hexdigest()
    
    return f"Sistem berjalan. Hash MD5: {konfigurasi_hash_lemah}"