import asyncio

from app.database import AsyncSessionLocal
from app.models.equipment import Equipment
from app.models.enums import EquipmentStatus, JobPriority, JobStatus
from app.models.farm import Farm
from app.models.field_job import FieldJob
from app.models.operator import Operator
from app.models.service_report import ServiceReport


async def seed() -> None:
    async with AsyncSessionLocal() as db:

        farm1 = Farm(
            name="Sarasota Orange Field",
            location_region="SE, United States",
            capacity=10,
            supervisor_id=101,
        )

        farm2 = Farm(
            name="Florence Vineyard",
            location_region="S, Europe",
            capacity=5,
            supervisor_id=102,
        )

        db.add_all([farm1, farm2])
        await db.flush()

        op1 = Operator(
            name="John Johnson",
            farm_id=farm1.id,
        )

        op2 = Operator(
            name="James Jameson",
            farm_id=farm2.id,
        )

        op3 = Operator(
            name="Bob Smith",
            farm_id=farm1.id,
        )

        db.add_all([op1, op2, op3])
        await db.flush()

        equip1 = Equipment(
            serial_number="ABCD-1",
            model="RW8760",
            status=EquipmentStatus.IDLE,
            fuel_level=67.8,
            facility_id=farm1.id,
        )

        equip2 = Equipment(
            serial_number="ABCD-2",
            model="RW8760",
            status=EquipmentStatus.IN_USE,
            fuel_level=21.1,
            facility_id=farm1.id,
        )

        equip3 = Equipment(
            serial_number="QRST-1",
            model="CASE60",
            status=EquipmentStatus.MAINTENANCE,
            fuel_level=99.0,
            facility_id=farm2.id,
        )

        equip4 = Equipment(
            serial_number="GOOD-1",
            model="NHTR70",
            status=EquipmentStatus.IN_USE,
            fuel_level=9.6,
            facility_id=farm1.id,
        )

        db.add_all([equip1, equip2, equip3, equip4])
        await db.flush()

        field_job1 = FieldJob(
            title="Harvest Grapes",
            priority=JobPriority.CRITICAL,
            status=JobStatus.IN_PROGRESS,
            equipment_id=equip2.id,
            operator_id=op1.id,
        )

        field_job2 = FieldJob(
            title="Sow Oranges",
            priority=JobPriority.MEDIUM,
            status=JobStatus.PENDING,
            equipment_id=equip3.id,
            operator_id=op2.id,
        )

        db.add_all([field_job1, field_job2])
        await db.flush()

        svr1 = ServiceReport(
            file_url="example1234.txt",
            notes="Everything going as planned",
            field_job_id=field_job1.id,
        )

        svr2 = ServiceReport(
            file_url="anotherexample11111111.txt",
            notes="This job is going great!!!!",
            field_job_id=field_job2.id,
        )

        db.add_all([svr1, svr2])
        await db.commit()


async def main():
    await seed()
    print("Seeding complete.")


if __name__ == "__main__":
    asyncio.run(main())