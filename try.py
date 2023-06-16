# # from typing import Any, Text, Dict, List

# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# # from rasa_sdk.events import SlotSet
# # import random
# # import requests
# # from utils.text_matcher import TextMatcher


# # class CustomAction(Action):
# #     def __init__(self, intent, entity, endpoint, value_to_replace, use_id=True, api_has_result=True, api_endpoint_name=None, **kwargs):
# #         '''api_endpoint_names, ['domain_count, 'by_domain_name']'''
# #         self.action = f"action_{intent}"
# #         self.response = f"upper_{intent}"
# #         self.entity = entity
# #         self.endpoint = endpoint
# #         self.use_id = use_id
# #         self.api_has_result = api_has_result
# #         self.value_to_replace = value_to_replace

# #         if not self.use_id:
# #             if not api_endpoint_name:
# #                 raise 'You must specify your api end point name'
# #             tm = TextMatcher(api_endpoint=api_endpoint_name)

# #     def name(self) -> Text:
# #         return self.action

# #     def run(
# #         self,
# #         dispatcher: CollectingDispatcher,
# #         tracker: Tracker,
# #         domain: Dict[Text, Any],
# #     ) -> List[Dict[Text, Any]]:

# #         entity = next(tracker.get_latest_entity_values(self.entity), None)

# #         if not self.use_id:
# #             entity = tm.find_best_match(entity)

# #         response = requests.get(
# #             f"{self.endpoint}={entity}"
# #         )

# #         if response.status_code == 200:
# #             data = response.json()
# #             if self.api_has_result:
# #                 result_value = data[value_needed]
# #             else:
# #                 result_value = data['results'][value_needed]
# #         else:
# #             dispatcher.utter_message(
# #                 text="Sorry, we could not retrieve the data from the API."
# #             )
# #             return []

# #         dispatcher.utter_message(
# #             response=self.response,
# #             domain_name=domain_name,
# #             domain_count=result_value,
# #         )

# #         return [
# #             SlotSet("domain_name", domain_name),
# #             SlotSet("domain_count", domain_count),
# #         ]

# # DomainCountAction = CustomAction(
# #     intent="get_domain_count",
# #     entity="domain_name",
# #     endpoint=f"http://127.0.0.1:8000/count/domain_name",
# #     value_needed='domain_count'
# # )


# # # class MyClass:
# # #     def __init__(self, **kwargs: Any):
# # #         for name, value in kwargs.items():
# # #             setattr(self, name, value)


# # # # Create an instance of MyClass with a property named "my_var" and value 42
# # # obj = MyClass(my_var=42)

# # # # Access the value of the property directly
# # # my_var_value = obj.my_var


# # # print(my_var_value)

# # # print(type(DomainCountAction.entity))
# # # print(type(DomainCountAction))

# # # myStr = "x=5"
# # # exec(myStr)
# # # print(type(x))


# # # myStr = "domain"
# # # myVal = "pythonforbeginners.com"
# # # myTemplate = '{} = "{}"'
# # # statement = myTemplate.format(myStr, myVal)
# # # exec(statement)
# # # print(domain)


# # # # def create_action_class(intent, endpoint, entity, api_endpoint: str) -> Type[Action]:
# # # #     tm = TextMatcher(api_endpoint=api_endpoint)

# # # #     class CustomAction(Action):
# # # #         def name(self) -> Text:
# # # #             return f"action_{intent}"

# # # #         def run(
# # # #             self,
# # # #             dispatcher: CollectingDispatcher,
# # # #             tracker: Tracker,
# # # #             domain: Dict[Text, Any],
# # # #         ) -> List[Dict[Text, Any]]:

# # # #             domain_name = next(tracker.get_latest_entity_values(entity), None)
# # # #             domain_name = tm.find_best_match(domain_name)

# # # #             response = requests.get(f'{endpoint}domain_name}")

# # # #             if response.status_code == 200:
# # # #                 data = response.json()
# # # #                 domain_count = data["domain_count"]
# # # #             else:
# # # #                 dispatcher.utter_message(
# # # #                     text="Sorry, we could not retrieve the data from the API."
# # # #                 )
# # # #                 return []

# # # #             dispatcher.utter_message(
# # # #                 response="utter_{intent}",
# # # #                 domain_name=domain_name,
# # # #                 domain_count=domain_count,
# # # #             )

# # # #             return [
# # # #                 SlotSet("domain_name", domain_name),
# # # #                 SlotSet("domain_count", domain_count),
# # # #             ]

# # # #     return CustomAction


# # # ActionDomainCount = create_action_class(intent="get_domain_count", entity='domain_name',
# # # endpoint=f"http://127.0.0.1:8000/count/domain_name=",
# # # )


# # # def get_entity_value(   
# # #         entity: str,
# # #         lower = 1,
# # #         upper = 3, 
# # #         ):

# # #     flag = False

# # #     if not entity_value:
# # #         message = f"Please provide the {entity_value} value."
# # #         return entity_value, message, flag

# # #     if entity_value not in list(range(lower, upper + 1)):
# # #         message = f'Please provide an existing {entity_value} value'
# # #         return entity_value, message, flag

# # #     try:
# # #         entity_value = int(entity_value)
# # #         flag = True
# # #         return entity_value, message, flag
# # #     except:
# # #         message = f"{entity_value} value must be an integer value"
# # #         return entity_value, message, flag



# # # print(get_entity_value('domain_name'))


# def get_entity_value(   
#         entity: str,
#         lower = 1,
#         upper = 3, 
#         ):

#     flag = False

#     if not entity_value:
#         message = f"Please provide the {entity_value} value."
#         return entity_value, message, flag

#     if entity_value not in list(range(lower, upper + 1)):
#         message = f'Please provide an existing {entity_value} value'
#         return entity_value, message, flag

#     try:
#         entity_value = int(entity_value)
#         flag = True
#         return entity_value, message, flag
#     except:
#         message = f"{entity_value} value must be an integer value"
#         return entity_value, message, flag
