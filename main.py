import requests

#URL dell'API
url = "https://jsonplaceholder.typicode.com/users"


# Richiesta GET
response = requests.get(url)

#controlliamo lo status code
if response.status_code == 200:
    utenti = response.json()  # JSON -> lista dict
    for u in utenti:
        print(f"{u['id']}: {u['name']} - {u['email']}")

else:
    print(f"Errore: {response.status_code}")