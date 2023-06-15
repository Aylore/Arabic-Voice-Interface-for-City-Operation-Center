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


class ActionDomainCount(Action):
    def name(self) -> Text:
        return "action_domain_count"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the value of the domainName entity from the user's message
        domain_name = next(tracker.get_latest_entity_values("domainName"), None)
        
        if domain_name is None:
            # Send a message to the user asking for the domainName value
            dispatcher.utter_message(text="Please provide the domainName value.")
            return []
        
        # Perform your desired logic using the alert_id value
        if domain_name:
            domain_count = random.randint(1, 1000)
        
        # dispatcher.utter_message(text=f"The domain count of the {domain_name} is {domain_count}.")

        # Send the response to the user and set the domainName, domainCount slot
        dispatcher.utter_message(
            response="utter_get_domain_count",
            domainName=domain_name,
            domainCount=domain_count
        )

        return [SlotSet("domainName", domain_name), SlotSet("domainCount", domain_count)]


class ActionGetDomainId(Action):
    def name(self) -> Text:
        return "action_get_domain_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the value of the domainName entity from the user's message
        domain_name = next(tracker.get_latest_entity_values("domainName"), None)
        
        if domain_name is None:
            # Send a message to the user asking for the domainName value
            dispatcher.utter_message(text="Please provide the domainName value.")
            return []
        
        # Perform your desired logic using the alert_id value
        if domain_name:
            domain_id = random.randint(1, 1000)
        
        # Send the response to the user and set the domainName, domainCount slot
        dispatcher.utter_message(
            response="utter_get_domain_count",
            domainName=domain_name,
            domainId=domain_id
        )

        return [SlotSet("domainName", domain_name), SlotSet("domainId", domain_id)]


class ActionAlertIdAlertStatus(Action):
    def name(self) -> Text:
        return "action_by_alert_id_alert_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the value of the domainName entity from the user's message
        alert_id = next(tracker.get_latest_entity_values("alertId"), None)
        
        if alert_id is None:
            # Send a message to the user asking for the domainName value
            dispatcher.utter_message(text="Please provide the alertId value.")
            return []
        
        # Perform your desired logic using the alert_id value
        if alert_id:
            opened = random.choice(['opened', 'closed'])
        
        # Send the response to the user and set the domainName, domainCount slot
        dispatcher.utter_message(
            response="utter_by_alert_id_alert_status",
            alertId=alert_id,
            opened=opened,
        )

        return [SlotSet("alertId", alert_id), SlotSet("opened", opened)]

class AlertClosureReason(Action):
    def name(self) -> Text:
        return "action_by_alert_closure_reason"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the value of the alertId entity from the user's message
        alert_id = next(tracker.get_latest_entity_values("alertId"), None)
        
        if alert_id is None:
            # Send a message to the user asking for the alertId value
            dispatcher.utter_message(text="Please provide the alertId value.")
            return []
        
        # Perform your desired logic using the alert_id value
        if int(alert_id) > 5:
            closure_reason = "Bigger than five"
        else:
            closure_reason = "Less than five"
        
        # Send the response to the user and set the closureReason slot
        dispatcher.utter_message(
            response="utter_by_alert_id_closure_reason",
            alertId=alert_id,
            closureReason=closure_reason
        )
        return [SlotSet("alertId", alert_id), SlotSet("closureReason", closure_reason)]



class AlertDomainAssociatied(Action):
    def name(self) -> Text:
        return "action_by_alert_id_domain_id_associated_alert"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the value of the alertId entity from the user's message
        alert_id = next(tracker.get_latest_entity_values("alertId"), None)
        
        if alert_id is None:
            # Send a message to the user asking for the alertId value
            dispatcher.utter_message(text="Please provide the alertId value.")
            return []
        
        # Perform your desired logic using the alert_id value
        if alert_id:
            domain_id = random.randint(1, 1000)
        
        # Send the response to the user and set the closureReason slot
        dispatcher.utter_message(
            response="utter_by_alert_id_domain_id_associated_alert",
            alertId=alert_id,
            domainId=domain_id
        )
        return [SlotSet("alertId", alert_id), SlotSet("domainId", domain_id)]
