from sqlmodel import Session, create_engine
from app.core.config import settings

engine = create_engine(settings.DB_URL, echo=True)

def get_session():
    """
    🛡 Read-only session — KHÔNG được gọi session.add() hoặc commit()
    """
    with Session(engine) as session:
        yield session