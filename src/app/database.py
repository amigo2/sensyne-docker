from uuid import UUID
from typing import List

from . models import Reading, UnitEnum


db: List[Reading] = [
    Reading(
        reading_uuid=UUID("1faafa60-c19a-4dd1-b5b0-e1d55f9464d4"),
        patient_uuid="22c685ae-9249-4c84-9b6e-d0e3537be66e",
        value="5.5",
        unit=UnitEnum.MMOL,
        recorded_at="2021-01-01T09:15:00+00:00"
    ),
    Reading(
        reading_uuid=UUID("70da0f35-317c-4a1a-a549-2f8e786b7cef"),
        patient_uuid="22c685ae-9249-4c84-9b6e-d0e3537be66e",
        value="7.2",
        unit=UnitEnum.MG,
        recorded_at="2021-01-01T12:30:00+00:00"
    ),
    Reading(
        reading_uuid=UUID("8a041e90-6c11-4b21-b345-cddbd57b8a1b"),
        patient_uuid="22c685ae-9249-4c84-9b6e-d0e3537be66e",
        value="5.1",
        unit=UnitEnum.MMOL,
        recorded_at="2021-01-01T16:45:00+00:00"
    )
]
