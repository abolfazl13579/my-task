import csv
import requests

API_URL= "https://openlibrary.org/search.json"

SEARCH_QUERY = "python programming"

LIMIT = 50

MIN_YEAR = 2000

OUTPUT_FILE = "books_after_2000.csv"

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

books = data.get("docs", [])

print("Number of books :", len(books))

filtered_books = []

seen_keys = set()


for book in books:
    year = book.get("first_publish_year")
    key = book.get("key", "")

    if year is None:
        continue
    
    if year > MIN_YEAR and key not in seen_keys:
        seen_keys.add(key)

        title = book.get("title", "Unknown")

        authors = book.get("author_name", [])
        if len(authors) > 0:
            author = ", ".join(authors)
        else:
            author = "Unknown"

        filtered_books.append(
            {
                "title": title,
                "author": author,
                "first_publish_year": year,
                "openlibrary_key": key,
            }
        )

print("Number of books after 2000 (without duplicates):", len(filtered_books))

with open(OUTPUT_FILE , "w" , newline="" ,encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["title" , "author" , "first_publish_year", "openlibrary_key"]  
    )
    writer.writeheader()
    for book in filtered_books:
        writer.writerow(book)

print("The file was saved." , OUTPUT_FILE)

