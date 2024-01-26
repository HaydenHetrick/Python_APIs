import requests
import csv

def search_book(book_title):
    url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}"
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        books = data["items"]
        with open("book_search_results.csv", "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Volume ID', 'Title', 'Published Date', 'Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for book in books:
                volume_info = book.get("volumeInfo", {})
                volume_id = book.get("id", "")
                title = volume_info.get("title", "N/A")
                published_date = volume_info.get("publishedDate", "N/A")
                description = volume_info.get("description", "N/A")

                writer.writerow({'Volume ID': volume_id,
                                 'Title': title,
                                 'Published Date': published_date,
                                 'Description': description})

                print(f"Volume ID: {volume_id}")
                print(f"Title: {title}")
                print(f"Published Date: {published_date}")
                print(f"Description: {description}")
                print("\n")

    else:
        print("No books found for the given title.")

if __name__ == "__main__":
    book_title = input("Enter the book you'd like to search: ")
    search_book(book_title)
