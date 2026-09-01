from enum import Enum

class EquipmentStatus(str, Enum):
    IDLE = "Idle"
    IN_USE = "In-Use"
    MAINTENANCE = "Maintenance"
    RETIRED = "Retired"

class JobPriority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    CRITICAL = "Critical"

class JobStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In-Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"

class UserRole(str, Enum):
    OPERATIONS_ADMIN = "Farm Operations Admin"
    FIELD_HAND = "Field Hand"
    AUDITOR = "Auditor"