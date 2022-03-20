from fastapi import FastAPI, HTTPException
from uuid import UUID

from . database import db
from . models import Reading

app = FastAPI()


@app.get("/v1/reading")
async def fetch_readings() -> None:
    try:
        return db
    except Exception as e:
        raise HTTPException(status_code=204, detail=" No content")


@app.post("/v1/reading")
async def register_readings(reading: Reading):
    try:
        db.append(reading)
        return {"reading_uuid": f"reading is created with"
                            f" reading id: {reading.reading_uuid}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/v1/reading/{reading_uuid}")
async def detailed_reading_uuid(reading_uuid: UUID):
    try:
        for readings in db:
            if readings.reading_uuid == reading_uuid:
                context = {
                    "reading_uuid": readings.reading_uuid,
                    "patient_uuid": readings.patient_uuid,
                    "value": readings.value,
                    "unit": readings.unit,
                    "recorded_at": readings.recorded_at
                }
                return context
            if readings.reading_uuid != reading_uuid:
                raise HTTPException(status_code=400, detail="Detailed reading not found")
    except Exception as e:
        raise HTTPException(status_code=404, detail="Detailed reading not found")


@app.put("/v1/reading/{reading_uuid}")
async def update_reading(reading_uuid:UUID, reading:Reading):
    try:
        for readings in db:
            if readings.reading_uuid == reading_uuid:
                readings.patient_uuid = reading.patient_uuid

                readings.value = reading.value
                readings.unit = reading.unit
                readings.recorded_at = reading.recorded_at
                return {"reading_uuid": f"reading been updated with"
                            f" reading id: {reading.reading_uuid}"}
            if readings.reading_uuid != reading_uuid:
                raise HTTPException(status_code=404, detail="Update reading not found")

    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))


@app.delete("/v1/reading/")
async def delete_reading(reading_uuid: UUID):
    try:
        for readings in db:
            if readings.reading_uuid == reading_uuid:
                db.remove(readings)
                return {"deleted": f"reading with reading id:"
                                   f" {readings.reading_uuid}, "
                                   f"has been successfully deleted."}
            if readings.reading_uuid != reading_uuid:
                raise HTTPException(status_code=404, detail="reading not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Not found")
