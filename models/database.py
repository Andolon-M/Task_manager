from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de conexión PostgreSQL
DATABASE_URL = "postgresql+psycopg2://postgres:bSYXUFJrXXionzlwTLUlxWZDlvnnVagC@junction.proxy.rlwy.net:49450/railway"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    import models.task  # Asegúrate de tener los modelos importados correctamente
    Base.metadata.create_all(bind=engine)
