from fastapi import APIRouter, Query
from app.services.tile_service import get_jobs_by_tile
from app.services.kpi_service import get_kpi_status

router = APIRouter()


@router.get("/tiles/{tilename}/jobs")
def fetch_jobs(tilename: str):

    jobs = get_jobs_by_tile(tilename)

    return {
        "tilename": tilename,
        "jobnames": jobs
    }


@router.get("/kpi-status")
def fetch_kpi_status(buildnumber: str, jobnames: str = Query(...)):

    job_list = jobnames.split(",")

    result = get_kpi_status(buildnumber, job_list)

    return result