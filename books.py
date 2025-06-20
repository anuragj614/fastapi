from fastapi import FastAPI

app = FastAPI()

books = [
    {"title": "Book One", "author": "Author A", "category": "Fiction"},
    {"title": "Book Two", "author": "Author B", "category": "Horror"},
    {"title": "Book Three", "author": "Author C", "category": "Thriller"},
    {"title": "Book Four", "author": "Author D", "category": "Fantasy"},
    {"title": "Book Five", "author": "Author E", "category": "Mystery"},
    {"title": "Book Six", "author": "Author F", "category": "Fantasy"},
    {"title": "Book Seven", "author": "Author B", "category": "Horror"},
    {"title": "Book Eight", "author": "Author H", "category": "Thriller"},
    {"title": "Book Nine", "author": "Author I", "category": "Horror"},
    {"title": "Book Ten", "author": "Author J", "category": "History"}
]


@app.get("/")
async def first_api():
    return {"message": "Hello"}

@app.get("/books")
async def get_books():
    return books

"""
    This is called path parameter and it is used to get a specific book by its title
"""

@app.get("/books/{book_title}")
async def get_book_by_title(book_title: str):
    for book in books:
        if book["title"].lower() == book_title.lower():
            return book
    return {"message": "Book not found"}



"""
    If you add another endpoint /books/mybooks, it will return the same response as /books/{dynamic_param} 
    because FastAPI sees the function in chronological order and matches the first one that fits the pattern.
    If you want to have a specific endpoint for /books/mybooks, you need to define it before the dynamic one.
"""
# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param: str):     #must be a string when when str is used
#     return {"dynamic_param": dynamic_param}

    

"""
    This is called query parameter and it is used to filter books by category.
    Example: /books/?category=Fiction
    It will return all books that belong to the Fiction category.
"""

@app.get("/books/")
async def read_book_by_category_query(category: str):
    books_to_return = []
    for book in books:
        try:
            if book.get("category").casefold() == category.casefold():
                books_to_return.append(book)   
        except KeyError:
            return {"message": "Category not found"}
        
    return books_to_return


@app.get("/books/{author}/")
async def read_book_by_author_category_query(author: str, category:str):
    books_to_return = []
    for book in books:
        try:
            if book.get("author").casefold() == author.casefold() and book.get("category").casefold() == category.casefold():
                books_to_return.append(book)
        except KeyError:
            return {"message": "Author or Category not found"}
    return books_to_return