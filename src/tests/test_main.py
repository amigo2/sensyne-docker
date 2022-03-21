from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_readings():
    response = client.get("/v1/reading")
    assert response.status_code == 200


def test_create_reading():
    response = client.post("/v1/reading",
                           json={
                                "reading_uuid": "1faafa60-c19a-4dd1-b5b0-e1d55f9464d4",
                                "patient_uuid": "22c685ae-9249-4c84-9b6e-d0e3537be66e",
                                "value": 5.5,
                                "unit": "mmol/L",
                                "recorded_at": "2021-01-01T09:15:00+00:00"
                            })
    assert response.status_code == 200
    assert response.json() == {
            'reading_uuid':
            'reading is created with reading id: 1faafa60-c19a-4dd1-b5b0-e1d55f9464d4'
            }


def test_detailed_view_reading():
    response = client.get("/v1/reading/1faafa60-c19a-4dd1-b5b0-e1d55f9464d4",
                          json={
                            "patient_uuid": "22c685ae-9249-4c84-9b6e-d0e3537be66e",
                            "value": 5.5,
                            "unit": "mmol/L",
                            "recorded_at": "2021-01-01T09:15:00+00:00"
                            })
    assert response.status_code == 200
    assert response.json() == {
        "reading_uuid": "1faafa60-c19a-4dd1-b5b0-e1d55f9464d4",
        "patient_uuid": "22c685ae-9249-4c84-9b6e-d0e3537be66e",
        "value": 5.5,
        "unit": "mmol/L",
        "recorded_at": "2021-01-01T09:15:00+00:00"
    }


def test_detailed_view_non_exists_and_fails():
    response = client.get("/v1/reading/unknown-reading-uuid")
    assert response.status_code == 422


def test_update_reading():
    response = client.put("/v1/reading/1faafa60-c19a-4dd1-b5b0-e1d55f9464d4",
                          json={
                                "patient_uuid": "22c685ae-9249-4c84-9b6e-d0e3537be66e",
                                "value": 5.5,
                                "unit": "mmol/L",
                                "recorded_at": "2021-01-01T09:15:00+00:00"
                            })
    assert response.status_code == 200


def test_update_non_existing_reading_fails():
    response = client.put(
        "/v1/reading/unknown-reading-uuid",
        json={
            "reading_uuid": "1faafa60-c19a-4dd1-b5b0-e1d55f9464d4",
            "patient_uuid": "22c685ae-9249-4c84-9b6e-d0e3537be66e",
            "value": 5.5,
            "unit": "mmol/L",
            "recorded_at": "2021-01-01T09:15:00+00:00"
        })
    assert response.status_code == 422


def test_delete_reading():
    response = client.delete("/v1/reading/?reading_uuid=1faafa60-c19a-4dd1-b5b0-e1d55f9464d4")
    assert response.status_code == 200
    assert response.json() == {
            "deleted":
            "reading with reading id: 1faafa60-c19a-4dd1-b5b0-e1d55f9464d4, has been successfully deleted."
            }


def test_delete_non_existing_reading_and_fails():
    response = client.delete("/v1/reading/?reading_uuid=1faafa60-c19a-4dd1-b5b0-e1d55f946444")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Not found"
    }



