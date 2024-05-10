# test_libreria.py
import requests

response = requests.get("https://g3w.uns.edu.ar/guarani3w/mesas_publica")
print("Status code:", response.status_code)
print("Response content:", response.text)