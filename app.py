import requests

# SonarQube akan menandai ini karena menggunakan HTTP (clear-text)
response = requests.get("http://internal-api.service/get-data")