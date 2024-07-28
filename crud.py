import asyncio

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import db_helper, User, Profile, Post


async def create_user(
    session: AsyncSession,
    username: str,
) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    # await print("user", user) хз почему падает
    return user


async def get_user_by_username(
    session: AsyncSession,
    username: str,
) -> User | None:
    stmt = select(User).where(User.username == username)
    # result: Result = await session.execute(stmt)
    # user: User | None = result.scalar_one_or_none()
    user = await session.scalar(stmt)
    print("found USER", username, user)
    return user


async def create_user_profile(
    session: AsyncSession,
    user_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
) -> Profile:
    profile = Profile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
    )
    session.add(profile)
    await session.commit()
    return profile


async def show_users_with_profiles(session: AsyncSession) -> list[User]:
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    for user in users:
        print(user)
        print(str(user.profile))


async def create_posts(
    session: AsyncSession,
    user_id: int,
    *post_titles: str,
) -> list[Post]:
    posts = [Post(title=title, user_id=user_id) for title in post_titles]
    session.add_all(posts)
    await session.commit()
    print(posts)
    return posts


async def main():
    async with db_helper.session_factory() as session:
        # await create_user(session=session, username="john")
        # await create_user(session=session, username="dana")
        user_dana = await get_user_by_username(session=session, username="dana")
        user_john = await get_user_by_username(session=session, username="john")
        # await get_user_by_username(session=session, username="bob")
        # await create_user_profile(
        #     session=session,
        #     user_id=user_john.id,
        #     first_name="John",
        # )
        # await create_user_profile(
        #     session=session,
        #     user_id=user_dana.id,
        #     first_name="DANA",
        #     last_name="White",
        # )
        await show_users_with_profiles(session)
        await create_posts(session, user_john.id, "SQLA_2.0", "ABABA", "Hello world")
        await create_posts(
            session,
            user_dana.id,
            "Programming is fun",
            "Its colour not color",
            "Oi mate",
        )


if __name__ == "__main__":
    asyncio.run(main())
