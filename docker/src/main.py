from fastapi import FastAPI
from controller.inventory import router as InventoryRouter

app = FastAPI()

app.include_router(InventoryRouter)
