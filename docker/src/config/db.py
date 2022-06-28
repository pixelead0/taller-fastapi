import databases
import sqlalchemy

DATABASE_URL = "postgresql://admin:admin@postgres/testdb"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
