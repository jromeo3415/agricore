from app.database import AsyncSessionLocal
from app.models.equipment import Equipment
from app.models.enums import EquipmentStatus

async def seed() -> None:
    async with AsyncSessionLocal() as db:
        equip1 = Equipment(
            serial_number="ABCD-1",
            model="RW8760",
            status=EquipmentStatus.IDLE,
            fuel_level=67.8,
            facility_id=1
        )

        