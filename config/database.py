from config.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = settings.database_url

engine = create_async_engine(DATABASE_URL, echo=True)
sync_engine = create_engine(DATABASE_URL.replace("aiomysql", "pymysql"))

# SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

AsyncSessionLocal= sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False
)

async def get_db():
   async with AsyncSessionLocal() as session:
      yield session