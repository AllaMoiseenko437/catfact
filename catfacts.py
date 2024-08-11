import requests

# Запрос 1
url_breeds = requests.get("https://catfact.ninja/breeds?limit")
print("Запрос 1:", url_breeds.text)
print(url_breeds.status_code)

# Запрос 2
url_fact_1 = requests.get("https://catfact.ninja/fact?limit=50&max_length=25")
print("Запрос 2:", url_fact_1.text)
print(url_fact_1.status_code)

#Запрос 3
url_fact_2 = "https://catfact.ninja/fact"
params_fact_2 = {
    "max_length": 50
}
response_fact_2 = requests.get(url_fact_2, params=params_fact_2)
print("Запрос 3: ", response_fact_2.text)
print(response_fact_2.status_code)
