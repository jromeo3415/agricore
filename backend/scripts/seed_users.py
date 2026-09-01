import asyncio

from app.models.enums import UserRole
from app.models.user import User
from app.database import AsyncSessionLocal
from app.security import hash_password

async def seed_users() -> None:
    async with AsyncSessionLocal() as db:
        db.add(User(username="joe", hashed_password=hash_password("12345678"), role=UserRole.OPERATIONS_ADMIN))

        await db.commit()

if __name__ == "__main__":
    asyncio.run(seed_users())