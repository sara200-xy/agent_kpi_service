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