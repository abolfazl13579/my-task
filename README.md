# OpenLibrary Books Fetcher

This script fetches book data from the OpenLibrary API, keeps only the books
published after the year 2000, removes duplicates, and saves the result to
a CSV file.

## Requirements

- Python 3
- requests library (install with `pip install requests`)

## How to run

Just run:

```
python task1.py
```

After it finishes, you will see `books_after_2000.csv` created in the same
folder.

## What it does

- Sends a request to the OpenLibrary search API for books about
  "python programming" and gets up to 50 results.
- Goes through the results and keeps only the books with a publish year
  after 2000. Books with no publish year, or duplicates, are skipped.
- Saves the remaining books to a CSV file with these columns: title,
  author, first_publish_year, and openlibrary_key.

## Note

Since the script only fetches 50 books and then filters them, the final
CSV file can have less than 50 rows. You can check `books_after_2000.csv`
in this repo to see a real output from running the script.
