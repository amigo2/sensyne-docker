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
        raise HTTPException(status_code=500, detail="No Connection with db ")


@app.post("/v1/reading")
async def register_readings(reading: Reading):
    try:
        db.append(reading)
        return {"reading_uuid": f"reading is created with "
                                f"reading id: {reading.reading_uuid}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/v1/reading/{reading_uuid}")
async def detailed_reading(reading_uuid: UUID):
    try:
        if not UUID(str(reading_uuid)):
            raise HTTPException(status_code=400, detail="not a valid UUID")
        else:
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
                elif readings.reading_uuid != reading_uuid:
                    pass
                else:
                    raise HTTPException(status_code=400, detail="Detailed reading not found")
    except Exception as e:
        raise HTTPException(status_code=404, detail="Detailed reading not found")


@app.put("/v1/reading/{reading_uuid}")
async def update_reading(reading_uuid: UUID, reading: Reading):
    try:
        if not UUID(str(reading_uuid)):
            raise HTTPException(status_code=404, detail="not a valid UUID")
        else:
            for readings in db:
                if readings.reading_uuid == reading_uuid:
                    readings.patient_uuid = reading.patient_uuid
                    readings.value = reading.value
                    readings.unit = reading.unit
                    readings.recorded_at = reading.recorded_at
                    return {"reading_uuid": f"reading been updated with"
                                f" reading id: {reading_uuid}"}
                elif readings.reading_uuid != reading_uuid:
                    pass
                else:
                    raise HTTPException(status_code=404, detail="Reading not found")

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/v1/reading/")
async def delete_reading(reading_uuid: UUID):
    try:
        for readings in db:
            if readings.reading_uuid == reading_uuid:
                db.remove(readings)
                return {"deleted": f"reading with reading id:"
                                   f" {reading_uuid}, "
                                   f"has been successfully deleted."}
            elif readings.reading_uuid != reading_uuid:
                pass
            else:
                raise HTTPException(status_code=404, detail="reading not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Not found")
