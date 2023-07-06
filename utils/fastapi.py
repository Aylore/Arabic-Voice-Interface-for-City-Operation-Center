"""
- The module provides 6 endpoints to retrieve data from 6 different JSON files. Each endpoint takes a parameter and returns the data that matches the parameter.
"""

import json
from fastapi import FastAPI, HTTPException

by_id_json_file_path = "src/rasa/data/json_data/by_alert_id.json"
by_job_json_file_path = "src/rasa/data/json_data/supervised_job_asset.json"
by_control_kpi_json_file_path = "src/rasa/data/json_data/control_kpi.json"
by_domain_id_json_file_path = "src/rasa/data/json_data/by_domain_id.json"
by_domain_count_json_file_path = "src/rasa/data/json_data/domain_count.json"
by_domain_name_json_file_path = "src/rasa/data/json_data/by_domain_name.json"

with open(by_id_json_file_path, "r") as file:
    # Load the JSON data
    dummy_data_by_id = json.load(file)

with open(by_job_json_file_path, "r") as file:
    # Load the JSON data
    dummy_data_by_job = json.load(file)

with open(by_control_kpi_json_file_path, "r") as file:
    # Load the JSON data
    dummy_data_by_control_kpi = json.load(file)

with open(by_domain_id_json_file_path, "r") as file:
    # Load the JSON data
    dummy_data_by_domain_id = json.load(file)

with open(by_domain_count_json_file_path, "r") as file:
    # Load the JSON data
    dummy_data_count_by_domain_name = json.load(file)

with open(by_domain_name_json_file_path, "r") as file:
    # Load the JSON data
    dummy_data_by_domain_name = json.load(file)

app = FastAPI()


# Endpoint to retrieve data by alert_id
@app.get("/by-id")
async def get_dummy_data_by_id(alert_id: int):
    """
    Retrieves data from by_alert_id.json by alert_id.

    This endpoint retrieves data from by_alert_id.json that matches the provided alert_id parameter.

    Args:
        alert_id: An integer representing the alert_id to match.

    Returns:
        A dictionary representing the data that matches the alert_id parameter.

    Raises:
        HTTPException: If no data matches the provided alert_id parameter.
    """
    for item in dummy_data_by_id:
        if alert_id == item["result"]["alert_id"]:
            return item
    raise HTTPException(status_code=404, detail="Please provide valid alert id")


@app.get("/supervised_job_asset={job_id}")
async def get_supervised_job_asset(job_id: int):
    """
    Retrieves data from supervised_job_asset.json by job_id.

    This endpoint retrieves data from supervised_job_asset.json that matches the provided job_id parameter.

    Args:
        job_id: An integer representing the job_id to match.

    Returns:
        A dictionary representing the data that matches the job_id parameter.

    Raises:
        HTTPException: If no data matches the provided job_id parameter.
    """
    for item in dummy_data_by_job:
        if job_id == item["result"]["supervised_job_asset"]:
            return item
    raise HTTPException(status_code=404, detail="Please provide valid job id")


@app.get("/control_kpi={kpi_id}")
async def get_control_kpi(kpi_id: int):
    """
    Retrieves data from control_kpi.json by kpi_id.

    This endpoint retrieves data from control_kpi.json that matches the provided kpi_id parameter.

    Args:
        kpi_id: An integer representing the kpi_id to match.

    Returns:
        A dictionary representing the data that matches the kpi_id parameter.

    Raises:
        HTTPException: If no data matches the provided kpi_id parameter.
    """
    for kpi in dummy_data_by_control_kpi:
        if kpi["id"] == kpi_id:
            return kpi
    raise HTTPException(status_code=404, detail="Please provide valid control kpi id")


@app.get("/domain_id={domain_id}")
async def get_dummy_data_by_domain_id(domain_id: int):
    """
    Retrieves data from by_domain_id.json by domain_id.

    This endpoint retrieves data from by_domain_id.json that matches the provided domain_id parameter.

    Args:
        domain_id: An integer representing the domain_id to match.

    Returns:
        A dictionary representing the data that matches the domain_id parameter.

    Raises:
        HTTPException: If no data matches the provided domain_id parameter.
    """
    for item in dummy_data_by_domain_id:
        if domain_id == item["result"]["id"]:
            return item
    raise HTTPException(status_code=404, detail="Please provide valid domain Id")


@app.get("/count/domain_name={domain_name}")
async def get_dummy_data_count_by_domain_name(domain_name: str):
    """
    Retrieves data from domain_count.json by domain_name.

    This endpoint retrieves data from domain_count.json that matches the provided domain_name parameter.

    Args:
        domain_name: A string representing the domain_name to match.

    Returns:
        A dictionary representing the data that matches the domain_name parameter.

    Raises:
        HTTPException: If no data matches the provided domain_name parameter.
    """
    for item in dummy_data_count_by_domain_name:
        if domain_name == item["domain_name"]:
            return item
    raise HTTPException(status_code=404, detail="Please provide valid domain name")


@app.get("/domain_name={domain_name}")
async def get_dummy_data_by_domain_name(domain_name: str):
    """
    Retrieves data from by_domain_name.json by domain_name.

    This endpoint retrieves data from by_domain_name.json that matches the provided domain_name parameter.

    Args:
        domain_name: A string representing the domain_name to match.

    Returns:
        A dictionary representing the data that matches the domain_name parameter.

    Raises:
        HTTPException: If no data matches the provided domain_name parameter.
    """
    for item in dummy_data_by_domain_name:
        if domain_name == item["result"]["domain_name"]:
            return item
    raise HTTPException(status_code=404, detail="Please provide valid domain name")
