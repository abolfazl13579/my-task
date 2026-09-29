import csv
import requests

API_URL= "https://openlibrary.org/search.json"

SEARCH_QUERY = "python programming"

LIMIT = 50

response=requests.get(
    API_URL,
    params={
        "q": SEARCH_QUERY,
        "limit":LIMIT,
        "fields": "title,author_name,first_publish_year,key",
    },
    timeout=20
)

response.raise_for_status()

data= response.json()

print(data)










