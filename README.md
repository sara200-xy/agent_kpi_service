# KPI Agent Service

Backend service for Azure AI Foundry agent tools.

## Tools

1. Get jobs by tile
2. Get KPI status from SQL database

## Tech Stack

FastAPI
Azure SQL
SQLAlchemy

## Run Locally

pip install -r requirements.txt

uvicorn app.main:app --reload


##Screenshot / Demo

The screenshot below were captured from a live deployment where a
Microsoft Foundry agent called this API via OpenAPI to analyze
CI pipeline health.

<img width="1068" height="474" alt="Agent response" src="https://github.com/user-attachments/assets/fa32c721-4c0c-42ad-a138-5a65822a10d8" />

