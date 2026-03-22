from fastapi import APIRouter, Query
from app.services.tile_service import get_jobs_by_tile
from app.services.kpi_service import get_kpi_status

router = APIRouter()


@router.get("/kpi-status")
def fetch_kpi_status(
    buildnumber: str,
    tilename: str | None = None,
    jobnames: str | None = Query(default=None)
):
    if tilename:
        jobs = get_jobs_by_tile(tilename)
    elif jobnames:
        jobs = [j.strip() for j in jobnames.split(",") if j.strip()]
    else:
        # FastAPI will return 200 unless you raise; keeping simple:
        return {"error": "Provide either tilename or jobnames."}

    if not jobs:
        return {
            "tilename": tilename,
            "buildnumber": buildnumber,
            "jobnames": [],
            "kpi": []
        }

    kpi_result = get_kpi_status(buildnumber, jobs)

    return {
        "tilename": tilename,
        "buildnumber": buildnumber,
        "jobnames": jobs,
        "kpi": kpi_result
    }