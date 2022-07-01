from datetime import date
from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class VentasIn(BaseModel):
    producto_id: int
    cliente_id: int
    monto: float
    fecha_venta: datetime = None

    @validator('fecha_venta', pre=True, always=True)
    def set_datetime_now(cls, fecha):
        return fecha or datetime.now()


class Ventas(BaseModel):
    id: int
    producto_id: int
    cliente_id: int
    monto: float
    fecha_venta: date
