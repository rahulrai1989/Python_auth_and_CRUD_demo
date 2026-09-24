from itertools import product

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from models import Products
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello, welcome to the Backend!"

products = [
    Products(id=1, name="Product 1", description="Description of Product 1", price=10.99, quantity=100),
    Products(id=2, name="Product 2", description="Description of Product 2", price=19.99, quantity=50),
    Products(id=3, name="Product 3", description="Description of Product 3", price=5.99, quantity=200),
    Products(id=4, name="Product 4", description="Description of Product 4", price=15.99, quantity=75)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(database_models.Products).count()

    if count == 0:
        for product in products:
            db.add(database_models.Products(**product.model_dump()))
        db.commit()
        db.close()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Products).all()

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    dp_product = db.query(database_models.Products).filter(database_models.Products.id == product_id).first()
    if dp_product:
        return dp_product

    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products")
def create_product(product: Products, db: Session = Depends(get_db)):
    db.add(database_models.Products(**product.model_dump()))
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "data": product.model_dump(),
            "message": "Product created successfully",
            "code": status.HTTP_201_CREATED
        }
    )

@app.put("/products/{id}")
def update_product(id: int, product: Products, db: Session = Depends(get_db)):
    dp_product = db.query(database_models.Products).filter(database_models.Products.id == id).first()
    if dp_product:
        dp_product.name = product.name
        dp_product.description = product.description
        dp_product.price = product.price
        dp_product.quantity = product.quantity
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "data": product.model_dump(),
                "message": "Product updated successfully",
                "code": status.HTTP_200_OK
            }
        )

    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    dp_product = db.query(database_models.Products).filter(database_models.Products.id == id).first()
    if dp_product:
        db.delete(dp_product)
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Product deleted successfully",
                "code": status.HTTP_200_OK
            }
        )

    raise HTTPException(status_code=404, detail="Product not found")