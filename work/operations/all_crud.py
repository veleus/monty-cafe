from sqlalchemy import func
from sqlalchemy.orm import Session
from model.tables import Warehouse, Product


def calculate_stock(db: Session):
    return db.query(Product, func.coalesce(func.sum(Warehouse.Quantity), 0).label('stock')). \
        outerjoin(Warehouse, Product.ProductID == Warehouse.ProductID).group_by(Product).all()
