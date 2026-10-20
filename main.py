
from fastapi import FastAPI, Path, Query

app = FastAPI()

items = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "electronics"
    },
    {
        "id": 2,
        "name": "Phone",
        "category": "electronics"
    },
    {
        "id": 3,
        "name": "Shirt",
        "category": "clothing"
    },
    {
        "id": 4,
        "name": "Shoes",
        "category": "clothing"
    },
]


@app.get("/item/{item_id}")
def get_product(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return {"data": item}

    return {"error": "Product Not found"}


@app.get("/search")
def search(category: str):
    filtered_items = [
        item for item in items
        if item["category"].lower() == category.lower()
    ]

    return {"data": filtered_items}


"""
A path parameter is part of the URL path and is used to identify a specific item

A query parameter is passed after ? in the URL and is used to filter or search for data
"""


books = [
    {"id": 1, "title": "Python Basics", "genre": "education"},
    {"id": 2, "title": "The Hobbit", "genre": "fantasy"},
    {"id": 3, "title": "Harry Potter", "genre": "fantasy"},
]


@app.get("/book/{book_id}")
def get_book(book_id: int = Path(..., description="The ID of the book")):
    for book in books:
        if book["id"] == book_id:
            return {"data": book}

    return {"error": "Book not found"}


@app.get("/books")
def search_books(genre: str = Query(..., description="The genre to search for")):
    filtered_books = [
        book for book in books
        if book["genre"].lower() == genre.lower()
    ]

    return {"data": filtered_books}