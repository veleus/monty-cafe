from pydantic import BaseModel
from typing import Optional
from datetime import date


class ProductGroup(BaseModel):
    GroupID: int
    Name: str
    Description: Optional[str]
    ParentGroupID: Optional[int]


class Product(BaseModel):
    ProductID: int
    Name: str
    Code: str
    Article: str
    Description: Optional[str]
    PurchasePrice: float
    SalePrice: float
    SupplierID: int
    GroupID: int
    Photo: Optional[bytes]
    ExternalCode: Optional[str]
    UnitOfMeasurement: Optional[str]
    NonReducibleBalance: int


class Supplier(BaseModel):
    SupplierID: int
    Name: str
    Address: str
    Contact: str
    TaxID: str
    Country: str
    Phone: str
    Email: str
    AverageDeliveryTime: int


class SupplierOrder(BaseModel):
    OrderID: int
    PlacementDate: date
    Amount: float
    Quantity: int
    Paid: bool
    DeliveryDate: date
    SupplierID: int


class ProductMovement(BaseModel):
    MovementID: int
    ProductID: int
    MovementType: str
    Quantity: int
    Date: date


class Warehouse(BaseModel):
    WarehouseID: int
    ProductID: int
    Quantity: int
    Location: str
    LastMovementDate: date


class TechCard(BaseModel):
    TechCardID: int
    Name: str
    Comments: Optional[str]


class Stage(BaseModel):
    StageID: int
    TechCardID: int
    Name: str
    Sequence: int
    Time: float
    Cost: float
    Description: Optional[str]


class ProductionOrder(BaseModel):
    OrderID: int
    PlacementDate: date
    StartDate: date
    EndDate: date
    TechCardID: int
    PlannedItems: int
    ProducedItems: int
    Comment: Optional[str]


class Material(BaseModel):
    MaterialID: int
    StageID: int
    ProductID: int
    Quantity: int


class Execution(BaseModel):
    ExecutionID: int
    OrderID: int
    StageID: int
    Performer: str
    QuantityPlanned: int
    QuantityDone: int
    StartDate: date
    EndDate: date


class ProductionPlanning(BaseModel):
    PlanningID: int
    OrderID: int
    StageID: int
    StartDate: date
    EndDate: date


class Payment(BaseModel):
    PaymentID: int
    EmployeeID: int
    Quantity: int
    Time: float
    Cost: float
    Date: date
    