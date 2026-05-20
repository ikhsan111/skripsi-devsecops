from flask import Flask
from flask_wtf.csrf import CSRFProtect, csrf

app = Flask(__name__)
csrf = CSRFProtect(app)

# Pola ini adalah analogi langsung dari @csrf_exempt di Django
# SonarQube akan mendeteksi decorator ini sebagai "Disabling CSRF protection"
@app.route('/update-profile', methods=['POST'])
@csrf.exempt 
def update_profile():
    return "Profil diperbarui tanpa proteksi CSRF"