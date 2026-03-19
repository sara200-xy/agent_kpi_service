from app.db.queries import query
from app.db.database import engine


def get_kpi_status(buildnumber: str, jobnames: list):

    if not jobnames:
        return []

    params = {
        "buildnumber": buildnumber,
        "jobnames": jobnames
    }

    with engine.connect() as session:
        result = session.execute(query, params)
        rows = [dict(row._mapping) for row in result]

    return rows