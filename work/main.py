from fastapi import FastAPI
import uvicorn
from database import engine, db
from model.tables import Base
from operations.all_crud import calculate_stock

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get('/main')
def update():
    return calculate_stock(db)


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
