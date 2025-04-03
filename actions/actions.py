from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# Utility function to match keywords
def keyword_match(keywords: List[str], message: Text) -> bool:
    message = message.lower()
    return any(keyword in message for keyword in keywords)


# 🏰 Action to set the house slot based on user's input
class ActionSetHouse(Action):
    def name(self) -> Text:
        return "action_set_house"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_input = tracker.latest_message.get("text", "").lower()
        houses = ["ignis", "aquae", "sylvae", "fulgur"]
        selected_house = None

        for house in houses:
            if house in user_input:
                selected_house = house.capitalize()
                break

        if selected_house:
            # dispatcher.utter_message(text=f"🏰 Wise choice — welcome to House {selected_house}!")
            return [SlotSet("house", selected_house)]
        else:
            dispatcher.utter_message(text="Please choose a valid house: Ignis, Aquae, Sylvae, or Fulgur.")
            return []


# 🎓 Assign house dynamically (fallback if no slot is set)
class ActionAssignHouse(Action):
    def name(self) -> Text:
        return "action_assign_house"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        house = tracker.get_slot("house")
        if not house:
            dispatcher.utter_message(response="utter_house_guide")
            return []
        return []


# 🧠 AI Quiz Check
class ActionCheckAIAnswer(Action):
    def name(self) -> Text:
        return "action_check_ai_answer"

    def run(self, dispatcher, tracker, domain):
        answer = tracker.latest_message.get("text", "")
        keywords = ["intelligence", "smart", "machines", "think", "mimic", "human"]
        if keyword_match(keywords, answer):
            dispatcher.utter_message(response="utter_correct_ai")
        else:
            dispatcher.utter_message(response="utter_wrong_ai")
        return []


# 🧾 NLP Quiz Check
class ActionCheckNLPAnswer(Action):
    def name(self) -> Text:
        return "action_check_nlp_answer"

    def run(self, dispatcher, tracker, domain):
        answer = tracker.latest_message.get("text", "")
        keywords = ["language", "text", "understand", "nlp", "natural language", "meaning"]
        if keyword_match(keywords, answer):
            dispatcher.utter_message(response="utter_correct_nlp")
        else:
            dispatcher.utter_message(response="utter_wrong_nlp")
        return []


# 🛡️ Cybersecurity Quiz Check
class ActionCheckCyberAnswer(Action):
    def name(self) -> Text:
        return "action_check_cyber_answer"

    def run(self, dispatcher, tracker, domain):
        answer = tracker.latest_message.get("text", "")
        keywords = ["security", "protect", "threats", "data", "network", "attacks", "hacking"]
        if keyword_match(keywords, answer):
            dispatcher.utter_message(response="utter_correct_cyber")
        else:
            dispatcher.utter_message(response="utter_wrong_cyber")
        return []


# 📊 Data Science Quiz Check
class ActionCheckDataAnswer(Action):
    def name(self) -> Text:
        return "action_check_data_answer"

    def run(self, dispatcher, tracker, domain):
        answer = tracker.latest_message.get("text", "")
        keywords = ["data", "insights", "patterns", "statistics", "analyze", "understanding"]
        if keyword_match(keywords, answer):
            dispatcher.utter_message(response="utter_correct_data")
        else:
            dispatcher.utter_message(response="utter_wrong_data")
        return []


# 🧱 DSA Quiz Check
class ActionCheckDSAAnswer(Action):
    def name(self) -> Text:
        return "action_check_dsa_answer"

    def run(self, dispatcher, tracker, domain):
        answer = tracker.latest_message.get("text", "")
        keywords = ["structure", "organize", "store", "data", "access", "linked list", "tree", "stack", "queue"]
        if keyword_match(keywords, answer):
            dispatcher.utter_message(response="utter_correct_dsa")
        else:
            dispatcher.utter_message(response="utter_wrong_dsa")
        return []
