"""main.py

This module is entry point into fast api application
"""
from fastapi import FastAPI, status
from models import ProductRequestModel, ProductResponseModel

# application object
app = FastAPI(
    title="Inventory Service",
    summary="Inventory Service for learning Fast API",
    version="1.0.0",
)


@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductRequestModel) -> ProductResponseModel:
    """Ths api will create product"""
    # store the product in database
    # generate a response
    return ProductResponseModel(
        id="1",
        name=product.name,
        sku=product.sku,
        price=product.price,
        stock=product.stock,
        description=product.description,
    )
