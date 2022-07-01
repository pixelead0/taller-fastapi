from fastapi import APIRouter
from typing import List
from datetime import datetime

from model.ventas import ventas
from pydantic_model.ventas import Ventas, VentasIn
from config.db import database

router = APIRouter()

@router.get("/ventas", response_model=List[Ventas])
async def mostrar_ventas():
    query = ventas.select()
    return await database.fetch_all(query)


@router.post("/ventas", response_model=Ventas)
async def crear_venta(venta: VentasIn):
    query = ventas.insert().values(
        producto_id = venta.producto_id, 
        cliente_id = venta.cliente_id, 
        monto = venta.monto,
        fecha_venta = venta.fecha_venta
    )
    id_ultimo_registro = await database.execute(query)
    return {**venta.dict(), "id": id_ultimo_registro}
