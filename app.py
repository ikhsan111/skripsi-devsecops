from flask import Flask

app = Flask(__name__)

# =====================================================================
# SKENARIO 3: Mengaktifkan Mode Debug secara Global
# Penulisan seperti ini pasti akan memicu alarm Security Hotspot
# Memancing Git agar mau push . .
# =====================================================================
app.config['DEBUG'] = True
app.debug = True

@app.route('/')
def index():
    return "Menguji Skenario 3: Debug Mode"