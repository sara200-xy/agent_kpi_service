from sqlalchemy import text, bindparam

query= text("""
        SELECT *
        FROM BuildPipelineStatus
        WHERE Buildnumber = :buildnumber
        AND JobName IN :jobnames
    """).bindparams(
        bindparam("jobnames", expanding=True)
    )