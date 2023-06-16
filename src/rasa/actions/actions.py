# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random
import requests
from utils.text_matcher import TextMatcher

tm_dc = TextMatcher(api_endpoint="domain_count")
tm_dn = TextMatcher(api_endpoint="by_domain_name")


class ActionDomainCount(Action):
    def name(self) -> Text:
        return "action_get_domain_count"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dc.find_best_match(domain_name)

        response = requests.get(
            f"http://127.0.0.1:8000/count/domain_name={domain_name}"
        )

        if response.status_code == 200:
            data = response.json()
            domain_count = data["domain_count"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_get_domain_count",
            domain_name=domain_name,
            domain_count=domain_count,
        )

        return [
            SlotSet("domain_name", domain_name),
            SlotSet("domain_count", domain_count),
        ]


class ActionGetdomain_id(Action):
    def name(self) -> Text:
        return "action_get_domain_id"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dc.find_best_match(domain_name)

        response = requests.get(
            f"http://127.0.0.1:8000/count/domain_name={domain_name}"
        )

        if response.status_code == 200:
            data = response.json()
            domain_id = data["domain_id"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_get_domain_count",
            domain_name=domain_name,
            domain_id=domain_id,
        )

        return [SlotSet("domain_name", domain_name), SlotSet("domain_id", domain_id)]


class ActionAlertStatus(Action): ########
    def name(self) -> Text:
        return "action_by_alert_id_alert_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []            

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            opened = data["result"]["opened"]
            opened = "open" if opened else "closed"
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_alert_status",
            alert_id=alert_id,
            opened=opened,
        )

        return [SlotSet("alert_id", alert_id), SlotSet("opened", opened)]


class Alertclosure_reason(Action):
    def name(self) -> Text:
        return "action_by_alert_closure_reason"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            closure_reason = data["result"]["closure_reason"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_closure_reason",
            alert_id=alert_id,
            closure_reason=closure_reason,
        )
        return [
            SlotSet("alert_id", alert_id),
            SlotSet("closure_reason", closure_reason),
        ]


class AlertDomainAssociatied(Action):
    def name(self) -> Text:
        return "action_by_alert_id_associated_domain"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            domain_id = data["result"]["domain_id"]

        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_associated_domain",
            alert_id=alert_id,
            domain_id=domain_id,
        )
        return [SlotSet("alert_id", alert_id), SlotSet("domain_id", domain_id)]


class AlertDomainAssociatied(Action):
    def name(self) -> Text:
        return "action_by_alert_id_message_id"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()

            message_id = data["result"]["message_id"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_message_id",
            alert_id=alert_id,
            message_id=message_id,
        )
        return [SlotSet("alert_id", alert_id), SlotSet("message_id", message_id)]


class AlertLastUpdate(Action):
    def name(self) -> Text:
        return "action_by_alert_id_last_update"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            last_updated_date = data["result"]["last_updated_date"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_last_update",
            alert_id=alert_id,
            last_updated_date=last_updated_date,
        )
        return [
            SlotSet("alert_id", alert_id),
            SlotSet("last_updated_date", last_updated_date),
        ]


class Alertvertical_id(Action):
    def name(self) -> Text:
        return "action_by_alert_id_vertical_id"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            vertical_id = data["result"]["vertical_id"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_vertical_id",
            alert_id=alert_id,
            vertical_id=vertical_id,
        )
        return [SlotSet("alert_id", alert_id), SlotSet("vertical_id", vertical_id)]


class Alertsop_ids(Action):
    def name(self) -> Text:
        return "action_by_alert_id_sop_ids"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            sop_ids = data["result"]["sop_ids"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_sop_ids", alert_id=alert_id, sop_ids=sop_ids
        )
        return [SlotSet("alert_id", alert_id), SlotSet("sop_ids", sop_ids)]


class Alertdevice_attribute(Action):
    def name(self) -> Text:
        return "action_by_alert_id_device_attribute"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            device_attribute = data["result"]["device_attribute"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_device_attribute",
            alert_id=alert_id,
            device_attribute=device_attribute,
        )
        return [
            SlotSet("alert_id", alert_id),
            SlotSet("device_attribute", device_attribute),
        ]


class AlertCriticality(Action):
    def name(self) -> Text:
        return "action_by_alert_id_criticality_level"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            criticality = data["result"]["criticality"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_criticality_level",
            alert_id=alert_id,
            criticality=criticality,
        )
        return [SlotSet("alert_id", alert_id), SlotSet("criticality", criticality)]


class Alertreading_value(Action):
    def name(self) -> Text:
        return "action_by_alert_id_reading_value"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            reading_value = data["result"]["reading_value"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_reading_value",
            alert_id=alert_id,
            reading_value=reading_value,
        )
        return [SlotSet("alert_id", alert_id), SlotSet("reading_value", reading_value)]


class Alertremoval_time(Action):
    def name(self) -> Text:
        return "action_by_alert_id_removal_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            removal_time = data["result"]["removal_time"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_removal_time",
            alert_id=alert_id,
            removal_time=removal_time,
        )
        return [SlotSet("alert_id", alert_id), SlotSet("removal_time", removal_time)]


class Alertgeneration_time(Action):
    def name(self) -> Text:
        return "action_by_alert_id_generation_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        alert_id = next(tracker.get_latest_entity_values("alert_id"), None)
        
        try:
            alert_id = int(alert_id)
        except:
            dispatcher.utter_message(text="Alert_id value must be an integer value")
            return []

        if alert_id is None:
            dispatcher.utter_message(text="Please provide the alert_id value.")
            return []

        if alert_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing alert_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/by-id?alert_id={alert_id}")

        if response.status_code == 200:
            data = response.json()
            generation_time = data["result"]["generation_time"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_alert_id_generation_time",
            alert_id=alert_id,
            generation_time=generation_time,
        )
        return [
            SlotSet("alert_id", alert_id),
            SlotSet("generation_time", generation_time),
        ]


class MetaDatasetInstances(Action):
    def name(self) -> Text:
        return "action_meta_features_dataset_instances"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Extract the value of the job_id entity from the user's message
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            num_instances = data["result"]["num_instances"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_dataset_instances",
            job_id=job_id,
            num_instances=num_instances,
        )
        return [SlotSet("job_id", job_id), SlotSet("num_instances", num_instances)]


class MetaDatasetRatio(Action):
    def name(self) -> Text:
        return "action_meta_features_dataset_ratio"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Extract the value of the job_id entity from the user's message
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            dataset_ratio = data["result"]["dataset_ratio"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_dataset_ratio",
            job_id=job_id,
            dataset_ratio=dataset_ratio,
        )
        return [SlotSet("job_id", job_id), SlotSet("dataset_ratio", dataset_ratio)]


class MetaDatasetRationNumToCat(Action):
    def name(self) -> Text:
        return "action_meta_features_ratio_num_to_cat"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            ratio_num_to_cat = data["result"]["ratio_num_to_cat"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_ratio_num_to_cat",
            job_id=job_id,
            ratio_num_to_cat=ratio_num_to_cat,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("ratio_num_to_cat", ratio_num_to_cat),
        ]


class MetaDatasetTotalMissingValues(Action):
    def name(self) -> Text:
        return "action_meta_features_total_missing_values"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []
        
        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            total_missing_Values = data["result"]["total_missing_Values"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_total_missing_values",
            job_id=job_id,
            total_missing_Values=total_missing_Values,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("total_missing_Values", total_missing_Values),
        ]


class MetaDatasetAverageMissingValues(Action):
    def name(self) -> Text:
        return "action_meta_features_avg_missing_values"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            avg_missing_values = data["result"]["avg_missing_values"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_avg_missing_values",
            job_id=job_id,
            avg_missing_values=avg_missing_values,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("avg_missing_values", avg_missing_values),
        ]


class MetaDatasetAverageMissingValues(Action):
    def name(self) -> Text:
        return "action_meta_features_num_cat_features"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            num_cat = data["result"]["num_cat"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_num_cat_features",
            job_id=job_id,
            num_cat=num_cat,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("num_cat", num_cat),
        ]


class MetaDatasetSumSymbols(Action):
    def name(self) -> Text:
        return "action_meta_features_sum_symbols"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            sum_symbols = data["result"]["sum_symbols"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_sum_symbols",
            job_id=job_id,
            sum_symbols=sum_symbols,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("sum_symbols", sum_symbols),
        ]


class MetaDatasetAverageSymbols(Action):
    def name(self) -> Text:
        return "action_meta_features_avg_symbols"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            avg_symbols = data["result"]["avg_symbols"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_avg_symbols",
            job_id=job_id,
            avg_symbols=avg_symbols,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("avg_symbols", avg_symbols),
        ]


class MetaDatasetStdSymbols(Action):
    def name(self) -> Text:
        return "action_meta_features_std_symbols"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            std_symbols = data["result"]["std_symbols"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_std_symbols",
            job_id=job_id,
            std_symbols=std_symbols,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("std_symbols", std_symbols),
        ]


class MetaDatasetNumStatiFeatures(Action):
    def name(self) -> Text:
        return "action_meta_features_num_stati_features"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            num_stati_features = data["result"]["num_stati_features"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_num_stati_features",
            job_id=job_id,
            num_stati_features=num_stati_features,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("num_stati_features", num_stati_features),
        ]


class MetaDatasetNumNonStatiFeatures(Action):
    def name(self) -> Text:
        return "action_meta_features_num_non_stati_features"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            num_non_stati_features = data["result"]["num_non_stati_features"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_num_non_stati_features",
            job_id=job_id,
            num_non_stati_features=num_non_stati_features,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("num_non_stati_features", num_non_stati_features),
        ]


class MetaDatasetNumFirstDifferences(Action):
    def name(self) -> Text:
        return "action_meta_features_num_first_differences"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Extract the value of the job_id entity from the user's message
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            num_1st_diff = data["result"]["num_1st_diff"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_num_first_differences",
            job_id=job_id,
            num_1st_diff=num_1st_diff,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("num_1st_diff", num_1st_diff),
        ]


class MetaDatasetNumSecondDifferences(Action):
    def name(self) -> Text:
        return "action_meta_features_num_second_differences"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            num_2st_diff = data["result"]["num_2st_diff"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_num_second_differences",
            job_id=job_id,
            num_2st_diff=num_2st_diff,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("num_2st_diff", num_2st_diff),
        ]


class MetaDatasetNumLaggedDifferences(Action):
    def name(self) -> Text:
        return "action_meta_features_num_lagged_features"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            num_lagged_features = data["result"]["num_lagged_features"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_num_lagged_features",
            job_id=job_id,
            num_lagged_features=num_lagged_features,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("num_lagged_features", num_lagged_features),
        ]


class MetaDatasetFeaturesPacf(Action):
    def name(self) -> Text:
        return "action_meta_features_pacf"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            pacf = data["result"]["pacf"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_pacf",
            job_id=job_id,
            pacf=pacf,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("pacf", pacf),
        ]


class MetaDatasetFeaturesSamplingRate(Action):
    def name(self) -> Text:
        return "action_meta_features_sampling_rate"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            sampling_rate = data["result"]["sampling_rate"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_sampling_rate",
            job_id=job_id,
            sampling_rate=sampling_rate,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("sampling_rate", sampling_rate),
        ]


class MetaDatasetFeaturesFractalDimension(Action):
    def name(self) -> Text:
        return "action_meta_features_fractal_dimension"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        job_id = next(tracker.get_latest_entity_values("job_id"), None)

        try:
            job_id = int(job_id)
        except:
            dispatcher.utter_message(text="job_id value must be an integer value")

        if job_id is None:
            dispatcher.utter_message(text="Please provide the job_id value.")
            return []

        if job_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing job_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/supervised_job_asset={job_id}")

        if response.status_code == 200:
            data = response.json()
            fractal_dim = data["result"]["fractal_dim"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_meta_features_fractal_dimension",
            job_id=job_id,
            fractal_dim=fractal_dim,
        )
        return [
            SlotSet("job_id", job_id),
            SlotSet("fractal_dim", fractal_dim),
        ]


###############
class ControlKpiEnabled(Action):
    def name(self) -> Text:
        return "action_check_control_kpi_enabled"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        kpi_id = next(tracker.get_latest_entity_values("control_kpi"), None)

        try:
            kpi_id = int(kpi_id)
        except:
            dispatcher.utter_message(text="kpi_id value must be an integer value")

        if kpi_id is None:
            dispatcher.utter_message(text="Please provide the kpi_id value.")
            return []

        if kpi_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing kpi_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/control_kpi={kpi_id}")

        if response.status_code == 200:
            data = response.json()
            is_enabled = data["is_enabled"]
            is_enabled = 'enabled' if is_enabled else 'disabled'
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_check_control_kpi_enabled",
            control_kpi=kpi_id,
            is_enabled=is_enabled,
        )
        return [
            SlotSet("control_kpi", kpi_id),
            SlotSet("is_enabled", is_enabled),
        ]


class ControlKpiDescribe(Action):
    def name(self) -> Text:
        return "action_describe_control_kpi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Extract the value of the control_kpi entity from the user's message
        kpi_id = next(tracker.get_latest_entity_values("control_kpi"), None)

        try:
            kpi_id = int(kpi_id)
        except:
            dispatcher.utter_message(text="kpi_id value must be an integer value")

        if kpi_id is None:
            dispatcher.utter_message(text="Please provide the kpi_id value.")
            return []

        if kpi_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing kpi_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/control_kpi={kpi_id}")

        if response.status_code == 200:
            data = response.json()
            description = data["description"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_describe_control_kpi",
            control_kpi=kpi_id,
            description=description,
        )
        return [
            SlotSet("control_kpi", kpi_id),
            SlotSet("description", description),
        ]


class ControlKpiExpression(Action):
    def name(self) -> Text:
        return "action_get_expression_control_kpi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        kpi_id = next(tracker.get_latest_entity_values("control_kpi"), None)

        try:
            kpi_id = int(kpi_id)
        except:
            dispatcher.utter_message(text="kpi_id value must be an integer value")

        if kpi_id is None:
            dispatcher.utter_message(text="Please provide the kpi_id value.")
            return []

        if kpi_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing kpi_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/control_kpi={kpi_id}")

        if response.status_code == 200:
            data = response.json()
            expression = data["expression"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_get_expression_control_kpi",
            control_kpi=kpi_id,
            expression=expression,
        )
        return [
            SlotSet("control_kpi", kpi_id),
            SlotSet("expression", expression),
        ]


class ControlKpiOutputAttribute(Action):
    def name(self) -> Text:
        return "action_get_output_attribute_control_kpi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Extract the value of the control_kpi entity from the user's message
        kpi_id = next(tracker.get_latest_entity_values("control_kpi"), None)

        try:
            kpi_id = int(kpi_id)
        except:
            dispatcher.utter_message(text="kpi_id value must be an integer value")

        if kpi_id is None:
            dispatcher.utter_message(text="Please provide the kpi_id value.")
            return []

        if kpi_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing kpi_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/control_kpi={kpi_id}")

        if response.status_code == 200:
            data = response.json()
            output_attribute_id = data["output_attribute_id"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_get_output_attribute_control_kpi",
            control_kpi=kpi_id,
            output_attribute_id=output_attribute_id,
        )
        return [
            SlotSet("control_kpi", kpi_id),
            SlotSet("output_attribute_id", output_attribute_id),
        ]


class ControlKpiCalendarUnit(Action):
    def name(self) -> Text:
        return "action_get_calendar_unit_control_kpi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        kpi_id = next(tracker.get_latest_entity_values("control_kpi"), None)

        try:
            kpi_id = int(kpi_id)
        except:
            dispatcher.utter_message(text="kpi_id value must be an integer value")

        if kpi_id is None:
            dispatcher.utter_message(text="Please provide the kpi_id value.")
            return []

        if kpi_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing kpi_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/control_kpi={kpi_id}")

        if response.status_code == 200:
            data = response.json()
            calendar_unit = data["calendar_unit"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_get_calendar_unit_control_kpi",
            control_kpi=kpi_id,
            calendar_unit=calendar_unit,
        )
        return [
            SlotSet("control_kpi", kpi_id),
            SlotSet("calendar_unit", calendar_unit),
        ]


class ControlKpiCreatedAt(Action):
    def name(self) -> Text:
        return "action_get_created_time_control_kpi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Extract the value of the control_kpi entity from the user's message
        kpi_id = next(tracker.get_latest_entity_values("control_kpi"), None)

        try:
            kpi_id = int(kpi_id)
        except:
            dispatcher.utter_message(text="kpi_id value must be an integer value")

        if kpi_id is None:
            dispatcher.utter_message(text="Please provide the kpi_id value.")
            return []

        if kpi_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing kpi_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/control_kpi={kpi_id}")

        if response.status_code == 200:
            data = response.json()
            created_at = data["created_at"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_get_created_time_control_kpi",
            control_kpi=kpi_id,
            created_at=created_at,
        )
        return [
            SlotSet("control_kpi", kpi_id),
            SlotSet("created_at", created_at),
        ]


class ControlKpiCreatedBy(Action):
    def name(self) -> Text:
        return "action_get_created_by_control_kpi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        kpi_id = next(tracker.get_latest_entity_values("control_kpi"), None)

        try:
            kpi_id = int(kpi_id)
        except:
            dispatcher.utter_message(text="kpi_id value must be an integer value")

        if kpi_id is None:
            dispatcher.utter_message(text="Please provide the kpi_id value.")
            return []

        if kpi_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing kpi_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/control_kpi={kpi_id}")

        if response.status_code == 200:
            data = response.json()
            created_by = data["created_by"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_get_created_by_control_kpi",
            control_kpi=kpi_id,
            created_by=created_by,
        )
        return [
            SlotSet("control_kpi", kpi_id),
            SlotSet("created_by", created_by),
        ]


class ControlKpiLastModifiedBy(Action):
    def name(self) -> Text:
        return "action_get_last_modified_by_control_kpi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        kpi_id = next(tracker.get_latest_entity_values("control_kpi"), None)

        try:
            kpi_id = int(kpi_id)
        except:
            dispatcher.utter_message(text="kpi_id value must be an integer value")

        if kpi_id is None:
            dispatcher.utter_message(text="Please provide the kpi_id value.")
            return []

        if kpi_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing kpi_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/control_kpi={kpi_id}")

        if response.status_code == 200:
            data = response.json()
            last_modified_by = data["last_modified_by"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_get_last_modified_by_control_kpi",
            control_kpi=kpi_id,
            last_modified_by=last_modified_by,
        )
        return [
            SlotSet("control_kpi", kpi_id),
            SlotSet("last_modified_by", last_modified_by),
        ]


class ControlKpiLastModifiedTime(Action):
    def name(self) -> Text:
        return "action_get_last_modified_time_control_kpi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        kpi_id = next(tracker.get_latest_entity_values("control_kpi"), None)

        try:
            kpi_id = int(kpi_id)
        except:
            dispatcher.utter_message(text="kpi_id value must be an integer value")

        if kpi_id is None:
            dispatcher.utter_message(text="Please provide the kpi_id value.")
            return []

        if kpi_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing kpi_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/control_kpi={kpi_id}")

        if response.status_code == 200:
            data = response.json()
            last_modified_at = data["last_modified_at"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_get_last_modified_time_control_kpi",
            control_kpi=kpi_id,
            last_modified_at=last_modified_at,
        )
        return [
            SlotSet("control_kpi", kpi_id),
            SlotSet("last_modified_at", last_modified_at),
        ]


class ControlKpiLastCalculatedTime(Action):
    def name(self) -> Text:
        return "action_get_last_calculated_time_control_kpi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        kpi_id = next(tracker.get_latest_entity_values("control_kpi"), None)

        try:
            kpi_id = int(kpi_id)
        except:
            dispatcher.utter_message(text="kpi_id value must be an integer value")

        if kpi_id is None:
            dispatcher.utter_message(text="Please provide the kpi_id value.")
            return []

        if kpi_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing kpi_id value")
            return []


        response = requests.get(f"http://127.0.0.1:8000/control_kpi={kpi_id}")

        if response.status_code == 200:
            data = response.json()
            last_calculated_at = data["last_calculated_at"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_get_last_calculated_time_control_kpi",
            control_kpi=kpi_id,
            last_calculated_at=last_calculated_at,
        )
        return [
            SlotSet("control_kpi", kpi_id),
            SlotSet("last_calculated_at", last_calculated_at),
        ]


#############
class DeviceOpenStatus(Action):
    def name(self) -> Text:
        return "action_domain_device_open_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_name={domain_name}")

        if response.status_code == 200:
            data = response.json()
            opened = data["result"]["opened"]
            opened = "opened" if opened else "closed"
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        # Send the response to the user and set the opened slot
        dispatcher.utter_message(
            response="utter_domain_device_open_status",
            domain_name=domain_name,
            opened=opened,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("opened", opened),
        ]


class DeviceCriticalityStatus(Action):
    def name(self) -> Text:
        return "action_domain_criticality_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_name={domain_name}")

        if response.status_code == 200:
            data = response.json()
            criticality = data["result"]["criticality"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        # Send the response to the user and set the criticality slot
        dispatcher.utter_message(
            response="utter_domain_criticality_status",
            domain_name=domain_name,
            criticality=criticality,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("criticality", criticality),
        ]


class DeviceClosureReason(Action):
    def name(self) -> Text:
        return "action_domain_closure_reason"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_name={domain_name}")

        if response.status_code == 200:
            data = response.json()
            closure_reason = data["result"]["closure_reason"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_domain_closure_reason",
            domain_name=domain_name,
            closure_reason=closure_reason,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("closure_reason", closure_reason),
        ]


class Devicereading_value(Action):
    def name(self) -> Text:
        return "action_domain_reading_value"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_name={domain_name}")

        if response.status_code == 200:
            data = response.json()
            reading_value = data["result"]["reading_value"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        # Send the response to the user and set the reading_value slot
        dispatcher.utter_message(
            response="utter_domain_reading_value",
            domain_name=domain_name,
            reading_value=reading_value,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("reading_value", reading_value),
        ]


class device_attributes(Action):
    def name(self) -> Text:
        return "action_domain_device_attributes"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_name={domain_name}")

        if response.status_code == 200:
            data = response.json()
            device_attribute = data["result"]["device_attribute"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        # Send the response to the user and set the device_attribute slot
        dispatcher.utter_message(
            response="utter_domain_device_attributes",
            domain_name=domain_name,
            device_attribute=device_attribute,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("device_attribute", device_attribute),
        ]


class Deviceremoval_time(Action):
    def name(self) -> Text:
        return "action_domain_removal_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_name={domain_name}")

        if response.status_code == 200:
            data = response.json()
            removal_time = data["result"]["removal_time"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_domain_removal_time",
            domain_name=domain_name,
            removal_time=removal_time,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("removal_time", removal_time),
        ]


class device_id(Action):
    def name(self) -> Text:
        return "action_domain_device_id"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_name={domain_name}")

        if response.status_code == 200:
            data = response.json()
            device_id = data["result"]["device_id"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_domain_device_id",
            domain_name=domain_name,
            device_id=device_id,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("device_id", device_id),
        ]


class device_name(Action):
    def name(self) -> Text:
        return "action_domain_device_name"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(
            f"http://127.0.0.1:8000/count/domain_name={domain_name}"
        )

        if response.status_code == 200:
            data = response.json()
            device_name = data["result"]["device_name"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_domain_device_name",
            domain_name=domain_name,
            device_name=device_name,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("device_name", device_name),
        ]


class device_longitude(Action):
    def name(self) -> Text:
        return "action_domain_device_longitude"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_name={domain_name}")

        if response.status_code == 200:
            data = response.json()
            device_longitude = data["result"]["device_longitude"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_domain_device_longitude",
            domain_name=domain_name,
            device_longitude=device_longitude,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("device_longitude", device_longitude),
        ]


class device_latitude(Action):
    def name(self) -> Text:
        return "action_domain_device_latitude"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_name={domain_name}")

        if response.status_code == 200:
            data = response.json()
            device_latitude = data["result"]["device_latitude"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        # Send the response to the user and set the device_latitude slot
        dispatcher.utter_message(
            response="utter_domain_device_latitude",
            domain_name=domain_name,
            device_latitude=device_latitude,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("device_latitude", device_latitude),
        ]


class generation_time(Action):
    def name(self) -> Text:
        return "action_domain_generation_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_name = next(tracker.get_latest_entity_values("domain_name"), None)
        domain_name = tm_dn.find_best_match(domain_name)

        if domain_name is None:
            dispatcher.utter_message(text="Please provide the domain_name value.")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_name={domain_name}")

        if response.status_code == 200:
            data = response.json()
            generation_time = data["result"]["generation_time"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_domain_generation_time",
            domain_name=domain_name,
            generation_time=generation_time,
        )
        return [
            SlotSet("domain_name", domain_name),
            SlotSet("generation_time", generation_time),
        ]


#############
class DomainDeviceStatus(Action):
    def name(self) -> Text:
        return "action_by_domain_id_device_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")

        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            opened = data["result"]["opened"]
            opened = "online" if opened else "offline"

        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_domain_id_device_status",
            domain_id=domain_id,
            opened=opened,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("opened", opened),
        ]


class DomainCriticalityStatus(Action):
    def name(self) -> Text:
        return "action_by_domain_id_criticality_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")

        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            criticality = data["result"]["criticality"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_domain_id_criticality_status",
            domain_id=domain_id,
            criticality=criticality,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("criticality", criticality),
        ]


class Domainclosure_reason(Action):
    def name(self) -> Text:
        return "action_by_domain_id_closure_reason"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")

        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            closure_reason = data["result"]["closure_reason"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_domain_id_closure_reason",
            domain_id=domain_id,
            closure_reason=closure_reason,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("closure_reason", closure_reason),
        ]

class Domainreading_value(Action):
    def name(self) -> Text:
        return "action_by_domain_id_reading_value"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")
            
        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            reading_value = data["result"]["reading_value"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        # Send the response to the user and set the reading_value slot
        dispatcher.utter_message(
            response="utter_by_domain_id_reading_value",
            domain_id=domain_id,
            reading_value=reading_value,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("reading_value", reading_value),
        ]


class Domaindevice_attribute(Action):
    def name(self) -> Text:
        return "action_by_domain_id_device_attributes"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")

        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            device_attribute = data["result"]["device_attribute"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        # Send the response to the user and set the device_attribute slot
        dispatcher.utter_message(
            response="utter_by_domain_id_device_attributes",
            domain_id=domain_id,
            device_attribute=device_attribute,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("device_attribute", device_attribute),
        ]


class Domainremoval_time(Action):
    def name(self) -> Text:
        return "action_by_domain_id_removal_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")

        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            removal_time = data["result"]["removal_time"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_domain_id_removal_time",
            domain_id=domain_id,
            removal_time=removal_time,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("removal_time", removal_time),
        ]


class Domaindevice_id(Action):
    def name(self) -> Text:
        return "action_by_domain_id_device_id"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")

        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            device_id = data["result"]["device_id"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_domain_id_device_id",
            domain_id=domain_id,
            device_id=device_id,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("device_id", device_id),
        ]


class Domaindevice_name(Action):
    def name(self) -> Text:
        return "action_by_domain_id_device_name"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")

        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            device_name = data["result"]["device_name"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_domain_id_device_name",
            domain_id=domain_id,
            device_name=device_name,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("device_name", device_name),
        ]


class Domaindevice_longitude(Action):
    def name(self) -> Text:
        return "action_by_domain_id_device_longitude"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")

        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            device_longitude = data["result"]["device_longitude"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_domain_id_device_longitude",
            domain_id=domain_id,
            device_longitude=device_longitude,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("device_longitude", device_longitude),
        ]


class Domaindevice_latitude(Action):
    def name(self) -> Text:
        return "action_by_domain_id_device_latitude"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")

        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            device_latitude = data["result"]["device_latitude"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        # Send the response to the user and set the device_latitude slot
        dispatcher.utter_message(
            response="utter_by_domain_id_device_latitude",
            domain_id=domain_id,
            device_latitude=device_latitude,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("device_latitude", device_latitude),
        ]


class Domaingeneration_time(Action):
    def name(self) -> Text:
        return "action_by_domain_id_generation_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        domain_id = next(tracker.get_latest_entity_values("domain_id"), None)

        try:
            domain_id = int(domain_id)
        except:
            dispatcher.utter_message(text="domain_id value must be an integer value")

        if domain_id is None:
            dispatcher.utter_message(text="Please provide the domain_id value.")
            return []

        if domain_id not in list(range(1, 4)):
            dispatcher.utter_message(text="Please provide an existing domain_id value")
            return []

        response = requests.get(f"http://127.0.0.1:8000/domain_id={domain_id}")

        if response.status_code == 200:
            data = response.json()
            generation_time = data["result"]["generation_time"]
        else:
            dispatcher.utter_message(
                text="Sorry, we could not retrieve the data from the API."
            )
            return []

        dispatcher.utter_message(
            response="utter_by_domain_id_generation_time",
            domain_id=domain_id,
            generation_time=generation_time,
        )
        return [
            SlotSet("domain_id", domain_id),
            SlotSet("generation_time", generation_time),
        ]
