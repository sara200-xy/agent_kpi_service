from fastapi import APIRouter, Query, HTTPException
from app.services.tile_service import get_jobs_by_tile
from app.services.kpi_service import get_kpi_status

router = APIRouter()

@router.get("/pipeline-kpi")
def get_pipeline_kpi(
    buildnumber: str = Query(...),
    tilename: str = Query(...)
):
    try:
        jobs = get_jobs_by_tile(tilename)

        if not jobs:
            raise HTTPException(status_code=404, detail="No jobs found for tile")

        kpi_data = get_kpi_status(buildnumber, jobs)

        return {
            "buildNumber": buildnumber,
            "tileName": tilename,
            "jobs": kpi_data
        }

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")