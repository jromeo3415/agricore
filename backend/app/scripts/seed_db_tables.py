from app.database import AsyncSessionLocal
from app.models.equipment import Equipment
from app.models.enums import EquipmentStatus, JobPriority, JobStatus
from app.models.farm import Farm
from app.models.field_job import FieldJob
from app.models.operator import Operator
from app.models.service_report import ServiceReport

async def seed() -> None:
    async with AsyncSessionLocal() as db:
        equip1 = Equipment(
            serial_number="ABCD-1",
            model="RW8760",
            status=EquipmentStatus.IDLE,
            fuel_level=67.8,
            facility_id=1
        )

        equip2 = Equipment(
                    serial_number="ABCD-2",
                    model="RW8760",
                    status=EquipmentStatus.IN_USE,
                    fuel_level=21.1,
                    facility_id=1
                )

        equip3 = Equipment(
                    serial_number="QRST-1",
                    model="CASE60",
                    status=EquipmentStatus.MAINTENANCE,
                    fuel_level=99.0,
                    facility_id=2
                )

        equip4 = Equipment(
                    serial_number="GOOD-1",
                    model="NHTR70",
                    status=EquipmentStatus.IN_USE,
                    fuel_level=9.6,
                    facility_id=1
                )

        farm1 = Farm(
            name="Sarasota Orange Field",
            location_region="SE, United States",
            capacity=10,
            supervisor_id=101
        )

        farm2 = Farm(
                    name="Florence Vineyard",
                    location_region="S, Europe",
                    capacity=5,
                    supervisor_id=102
                )

        field_job1 = FieldJob(
            title="Harvest Grapes",
            priority=JobPriority.CRITICAL,
            status=JobStatus.IN_PROGRESS,
            equipment_id=2,
            operator_id=1
        )

        field_job2 = FieldJob(
            title="Sow Oranges",
            priority=JobPriority.MEDIUM,
            status=JobStatus.PENDING,
            equipment_id=3,
            operator_id=2
        )

        op1 = Operator(
            name="John Johnson",
            farm_id=1,
        )

        op2 = Operator(
            name="James Jameson",
            farm_id=2,
        )

        op3 = Operator(
            name="Bob Smith",
            farm_id=1,
        )

        svr1 = ServiceReport(
            file_url="example1234.txt",
            notes="Everything going as planned",
            field_job_id=1
        )

        svr2 = ServiceReport(
            file_url="anotherexample11111111.txt",
            notes="This jobn is going grerat!!!!",
            field_job_id=2
        )

        db.add(equip1, equip2, equip3, equip4, farm1, farm2, field_job1, field_job2, op1, op2, op3, svr1, svr2)
        await db.commit()