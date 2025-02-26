from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Gunakan koneksi database dari environment (.env)
DATABASE_URL = settings.DATABASE_URL

# Gunakan `check_same_thread=False` untuk SQLite
engine = create_engine(DATABASE_URL, 
                       connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Generate tabel otomatis saat aplikasi dijalankan
def init_db():
    print("🔄 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created!")
