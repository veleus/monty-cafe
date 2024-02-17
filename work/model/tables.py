from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean, Date, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from database import Base


class ProductGroup(Base):
    __tablename__ = 'ProductGroups'

    GroupID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Description = Column(Text)
    ParentGroupID = Column(Integer, ForeignKey('ProductGroups.GroupID'))
    children = relationship("ProductGroup")


class Product(Base):
    __tablename__ = 'Products'

    ProductID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Code = Column(String(50))
    Article = Column(String(50))
    Description = Column(Text)
    PurchasePrice = Column(DECIMAL(10, 2))
    SalePrice = Column(DECIMAL(10, 2))
    SupplierID = Column(Integer, ForeignKey('Suppliers.SupplierID'))
    GroupID = Column(Integer, ForeignKey('ProductGroups.GroupID'))
    Photo = Column(BLOB)
    ExternalCode = Column(String(50))
    UnitOfMeasurement = Column(String(50))
    NonReducibleBalance = Column(Integer)
    supplier = relationship("Supplier")
    group = relationship("ProductGroup")


class Supplier(Base):
    __tablename__ = 'Suppliers'

    SupplierID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Address = Column(String(255))
    Contact = Column(String(100))
    TaxID = Column(String(50))
    Country = Column(String(100))
    Phone = Column(String(50))
    Email = Column(String(100))
    AverageDeliveryTime = Column(Integer)


class SupplierOrder(Base):
    __tablename__ = 'SupplierOrders'

    OrderID = Column(Integer, primary_key=True)
    PlacementDate = Column(Date)
    Amount = Column(DECIMAL(10, 2))
    Quantity = Column(Integer)
    Paid = Column(Boolean)
    DeliveryDate = Column(Date)
    SupplierID = Column(Integer, ForeignKey('Suppliers.SupplierID'))
    supplier = relationship("Supplier")


class ProductMovement(Base):
    __tablename__ = 'ProductMovements'

    MovementID = Column(Integer, primary_key=True)
    ProductID = Column(Integer, ForeignKey('Products.ProductID'))
    MovementType = Column(String(50))
    Quantity = Column(Integer)
    Date = Column(Date)
    product = relationship("Product")


class Warehouse(Base):
    __tablename__ = 'Warehouse'

    WarehouseID = Column(Integer, primary_key=True)
    ProductID = Column(Integer, ForeignKey('Products.ProductID'))
    Quantity = Column(Integer)
    Location = Column(String(255))
    LastMovementDate = Column(Date)
    product = relationship("Product")


class TechCard(Base):
    __tablename__ = 'TechCards'

    TechCardID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Comments = Column(Text)


class Stage(Base):
    __tablename__ = 'Stages'

    StageID = Column(Integer, primary_key=True)
    TechCardID = Column(Integer, ForeignKey('TechCards.TechCardID'))
    Name = Column(String(255))
    Sequence = Column(Integer)
    Time = Column(DECIMAL(10, 2))
    Cost = Column(DECIMAL(10, 2))
    Description = Column(Text)
    tech_card = relationship("TechCard")


class ProductionOrder(Base):
    __tablename__ = 'ProductionOrders'

    OrderID = Column(Integer, primary_key=True)
    PlacementDate = Column(Date)
    StartDate = Column(Date)
    EndDate = Column(Date)
    TechCardID = Column(Integer, ForeignKey('TechCards.TechCardID'))
    PlannedItems = Column(Integer)
    ProducedItems = Column(Integer)
    Comment = Column(Text)
    tech_card = relationship("TechCard")


class Material(Base):
    __tablename__ = 'Materials'

    MaterialID = Column(Integer, primary_key=True)
    StageID = Column(Integer, ForeignKey('Stages.StageID'))
    ProductID = Column(Integer, ForeignKey('Products.ProductID'))
    Quantity = Column(Integer)
    stage = relationship("Stage")
    product = relationship("Product")


class Execution(Base):
    __tablename__ = 'Execution'

    ExecutionID = Column(Integer, primary_key=True)
    OrderID = Column(Integer, ForeignKey('ProductionOrders.OrderID'))
    StageID = Column(Integer, ForeignKey('Stages.StageID'))
    Performer = Column(String(255))
    QuantityPlanned = Column(Integer)
    QuantityDone = Column(Integer)
    StartDate = Column(Date)
    EndDate = Column(Date)
    order = relationship("ProductionOrder")
    stage = relationship("Stage")


class ProductionPlanning(Base):
    __tablename__ = 'ProductionPlanning'

    PlanningID = Column(Integer, primary_key=True)
    OrderID = Column(Integer, ForeignKey('ProductionOrders.OrderID'))
    StageID = Column(Integer, ForeignKey('Stages.StageID'))
    StartDate = Column(Date)
    EndDate = Column(Date)
    order = relationship("ProductionOrder")
    stage = relationship("Stage")


class Payment(Base):
    __tablename__ = 'Payments'

    PaymentID = Column(Integer, primary_key=True)
    EmployeeID = Column(Integer)
    Quantity = Column(Integer)
    Time = Column(DECIMAL(10, 2))
    Cost = Column(DECIMAL(10, 2))
    Date = Column(Date)
    