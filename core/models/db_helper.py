from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from asyncio import current_task
from core.config import settings


class DataBaseHelper:
    def __init__(self, db_url, db_echo: bool = False):
        self.engine = create_async_engine(
            url=db_url,
            echo=db_echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        # session = self.session_factory()
        # async with session as sess:
        #     yield sess
        #     await session.close()
        #     # await session.remove() ЭТО ПРОСТО С АСИНХРОННОЙ СЕССИЕЙ
        session = self.get_session()
        yield session
        await session.close()


db_helper = DataBaseHelper(
    db_url=settings.db_url,
    db_echo=settings.db_echo,
)
