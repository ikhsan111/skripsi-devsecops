import os
from flask import request

# --- SKENARIO CWE-22 (Path Traversal) ---
# SonarQube akan mendeteksi ini sebagai Vulnerability (Critical)
@app.route('/read')
def read_file():
    filename = request.args.get('file')
    # Penyerang bisa melakukan traversal: ?file=../../etc/passwd
    with open(os.path.join('/var/www/uploads', filename), 'r') as f:
        return f.read()
# ----------------------------------------