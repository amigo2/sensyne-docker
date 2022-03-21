from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class UnitEnum(str, Enum):
    mol: str = "mmol/L"
    mg: str = "mg/dL"


class Reading(BaseModel):
    reading_uuid: Optional[UUID] = uuid4()
    patient_uuid: Optional[UUID] = uuid4()
    value: Optional[float] = None
    unit: UnitEnum = None
    recorded_at: Optional[datetime] = None
