from config.db import sqlalchemy, metadata

ventas = sqlalchemy.Table(
    "ventas",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("producto_id", sqlalchemy.Integer),
    sqlalchemy.Column("cliente_id", sqlalchemy.Integer),
    sqlalchemy.Column("monto", sqlalchemy.Float),
    sqlalchemy.Column("fecha_venta", sqlalchemy.DateTime, nullable=False),
)
