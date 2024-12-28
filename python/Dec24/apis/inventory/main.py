"""main.py

This module is entry point into fast api application
"""

from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
from view_models import ProductRequestModel, ProductResponseModel
from database import Base, SessionLocal, engine
from schema import Product


# now ensure all the tables are created
Base.metadata.create_all(bind=engine)


# Get database
def get_db():
    """
    This method gets the database connection
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# application object
app = FastAPI(
    title="Inventory Service",
    summary="Inventory Service for learning Fast API",
    version="1.0.0",
)


@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductRequestModel, db: Session = Depends(get_db)
) -> ProductResponseModel:
    """Ths api will create product"""
    # store the product in database
    db_product = Product(
        name = product.name,
        sku = product.sku,
        price = product.price,
        stock = product.stock,
        description = product.description
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    # generate a response
    return ProductResponseModel(
        id=db_product.id,
        name=product.name,
        sku=product.sku,
        price=product.price,
        stock=product.stock,
        description=product.description,
    )

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    """This method deletes the product based on id

    Args:
        id (int): product id
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Raises:
        HTTPException: Not Found

    Returns:
        message
    """
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted"}

