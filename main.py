from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
from db import get_db , engine
import services , models , schemas

app = FastAPI()

@app.get("/books", response_model=list[schemas.Book])
async def get_all_books(db: Session = Depends(get_db)):
    return services.get_books(db)

@app.get("/books/{book_id}", response_model= schemas.Book)
async def get_book(id: int, db: Session = Depends(get_db)):
    book = services.get_book(db,id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=schemas.Book)
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db, book)

@app.put("/books/{book_id}", response_model=schemas.Book)
async def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    updated_db = services.update_book(db, book, book_id)
    if not updated_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_db

@app.delete("/books/{book_id}", response_model=schemas.Book)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_book(db, book_id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail="Book not found")