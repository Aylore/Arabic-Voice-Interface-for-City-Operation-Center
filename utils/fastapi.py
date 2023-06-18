from fastapi import FastAPI, HTTPException
import json

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
    for item in dummy_data_by_id:
        if alert_id == item["result"]["alert_id"]:
            return item
    raise HTTPException(status_code=404, detail="Please provide valid alert id")


@app.get("/supervised_job_asset={job_id}")
async def get_supervised_job_asset(job_id: int):
    for item in dummy_data_by_job:
        if job_id == item["result"]["supervised_job_asset"]:
            return item
    raise HTTPException(status_code=404, detail="Please provide valid job id")


@app.get("/control_kpi={kpi_id}")
async def get_control_kpi(kpi_id: int):
    for kpi in dummy_data_by_control_kpi:
        if kpi["id"] == kpi_id:
            return kpi
    raise HTTPException(status_code=404, detail="Please provide valid control kpi id")


@app.get("/domain_id={domain_id}")
async def get_dummy_data_by_domain_id(domain_id: int):
    for item in dummy_data_by_domain_id:
        if domain_id == item["result"]["id"]:
            return item
    raise HTTPException(status_code=404, detail="Please provide valid domain Id")


@app.get("/count/domain_name={domain_name}")
async def get_dummy_data_count_by_domain_name(domain_name: str):
    for item in dummy_data_count_by_domain_name:
        if domain_name == item["domain_name"]:
            return item
    raise HTTPException(status_code=404, detail="Please provide valid domain name")


@app.get("/domain_name={domain_name}")
async def get_dummy_data_by_domain_name(domain_name: str):
    for item in dummy_data_by_domain_name:
        if domain_name == item["result"]["domain_name"]:
            return item
    raise HTTPException(status_code=404, detail="Please provide valid domain name")
