from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class UnitEnum(str, Enum):
    MMOL: str = "mmol/L"
    MG: str = "mg/dL"


class Reading(BaseModel):
    reading_uuid: Optional[UUID] = uuid4()
    patient_uuid: Optional[UUID] = uuid4()
    value: Optional[float] = None
    unit: UnitEnum
    recorded_at: Optional[datetime] = None
