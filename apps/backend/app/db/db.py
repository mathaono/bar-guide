from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

#Monta URL completa para acesso ao banco de dados
DATABASE_URL = settings.DATABASE_URL

#Cria o engine assíncrono
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

#Cria um sessionmaker com sessões assíncronas
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

#Base para os modelos (User, Bar e etc)
Base = declarative_base()

#Dependência que será usada nos endpoints para obter sessão
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session