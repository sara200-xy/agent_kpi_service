import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "kpilist.json"

with open(DATA_PATH) as f:
    kpi_data = json.load(f)


def get_jobs_by_tile(tilename: str):

    jobs = kpi_data.get(tilename)

    if not jobs:
        return []

    return jobs