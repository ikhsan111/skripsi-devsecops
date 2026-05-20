import os
from flask import Flask, request, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = '/var/www/uploads'

# --- SKENARIO KERENTANAN: CWE-22 (Path Traversal) ---
# SonarQube akan mendeteksi fungsi ini sebagai 'Vulnerability' 
# karena input 'filename' tidak divalidasi dan langsung digunakan untuk akses file.
@app.route('/download')
def download_file():
    filename = request.args.get('filename')
    # Penyerang bisa mengirim: ?filename=../../../../etc/passwd
    # SonarQube menangkap pola ini sebagai path traversal yang berbahaya.
    return send_from_directory(UPLOAD_FOLDER, filename)
# ----------------------------------------------------

if __name__ == '__main__':
    app.run()