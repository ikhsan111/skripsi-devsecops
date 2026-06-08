from flask import Flask

app = Flask(__name__)

# --- SKENARIO KERENTANAN: CWE-798 (Hardcoded Secret Key) ---
# Kunci rahasia didefinisikan secara statis di dalam source code.
# Ini sangat berbahaya karena kunci akan masuk ke dalam Version Control (Git).
app.config['SECRET_KEY'] = 'sangat-rahasia-banget-123456789'
# -----------------------------------------------------------

@app.route('/')
def hello_world():
    return 'Halo, sistem ini rentan!'

if __name__ == '__main__':
    app.run(debug=True)