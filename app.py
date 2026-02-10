from flask import Flask

# [TARGET 1] Rule: "Flask secret keys should not be disclosed"
# Anda punya rule ini di daftar. Ini harusnya langsung BLOCKER.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardcoded_secret_key_12345' 

# [TARGET 2] Rule: "Credentials should not be hard-coded"
# Anda punya rule ini. Variabel bernama 'password' dengan nilai string pasti kena.
def database_connect():
    user = "admin"
    password = "superSecretPassword123" # <--- INI HARUSNYA MELEDAK (BLOCKER)
    return True

# [TARGET 3] Rule: "Recursion should not be infinite"
# Anda punya rule ini. Fungsi yang memanggil dirinya sendiri tanpa henti.
def infinite_loop():
    return infinite_loop() # <--- Logic Error (BLOCKER)

# [TARGET 4] Rule: "The 'exec' statement should not be used"
# Anda punya rule ini di daftar (bawah).
def dynamic_code():
    code = "print('Bahaya')"
    exec(code) # <--- Security Risk (BLOCKER)

if __name__ == '__main__':
    database_connect()
    app.run()
