import os
import sys
import dialogflow_v2 as dialogflow
from uuid import uuid4
sys.path.append("..")
# from conf.Response import IntentResponse
import requests
import json
from flask import make_response, jsonify, request, Flask, url_for
import os
import re
from flask_cors import CORS
import jwt
import datetime
from functools import wraps


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'thisismykey'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.json["token"]
        if not token:
            return jsonify("Please login first")

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify("Please try to login again")

        return f(*args, **kwargs)

    return decorated


@app.route("/login", methods=['POST'])
def login():
    user = request.json["user"]
    password = request.json["password"]

    if user and password and  user == "1234" and password == {'words': [555953961, 2052564391, 1133070862, 1249910723], 'sigBytes': 16}:
        token = jwt.encode({'user': user, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, app.config['SECRET_KEY'])

        global_token = token
        return jsonify({'token': token.decode('UTF-8')})
    return jsonify("Please correct your username and password")


PATH = os.path.dirname(os.path.realpath(__file__))
DIALOGFLOW_PROJECT_ID = 'dentistappoinment'
GOOGLE_APPLICATION_CREDENTIALS = "DentistAppoinment-18719af8aa7b.json"
GOOGLE_APPLICATION_CREDENTIALS_PATH = os.path.join(PATH, GOOGLE_APPLICATION_CREDENTIALS)

class IntentResponse:
    def __init__(self, intent, message):
        self.intent = intent
        self.message = message

class FallbackResponse:
    def __init__(self, intent, message, confidence):
        self.intent = intent
        self.message = message
        self.confidence = confidence

session_id=uuid4()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS_PATH

project_id, session_id = DIALOGFLOW_PROJECT_ID, session_id
session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)



@app.route("/webhook", methods=['POST'])
@token_required
def detect_intent_texts(language_code='en'):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation.
    :param text: message
    :type str
    :param language_code: the language code of the language
    :type: str
    """

    token = request.json["token"]

    if not request.json:
        abort(400)
    text = request.json["text"]


    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)


    query = response.query_result.query_text
    intent = response.query_result.intent.display_name
    fullfillment = response.query_result.fulfillment_text

    if (intent == 'Default Fallback Intent' or intent == ""):
        return fullfillment

    if (intent == 'How can I book an appoinment'):
        return fullfillment

    if (intent == 'How can I cancel an appoinment'):
        return fullfillment


    if (intent == 'Greeting' or intent == 'Default Welcome Intent'):
        return fullfillment

    if (fullfillment == 'Asking for all dentists'):
        try:
            send_token = {'token' : token}
            url = requests.get("http://localhost:8000/v1/dentists", params=send_token)
            available = url.json()
            return available
        except:
            return jsonify("The dentist system is under maintenance")

    if (intent == "Give the details of Mike" or intent == "Give the details of Jim" or intent == "Give the details of Tracey" or intent == "Give the details of Oliver" or intent == "Give the details of Jack" or intent == "Give the details of Harry" or intent == "Give the details of Oscar" or intent == "Give the details of James" or intent == "Give the details of William" or intent == "Give the details of Joe"):
        if (fullfillment == 'Mike' or fullfillment == 'Jim' or fullfillment == 'Tracey' or fullfillment == 'Oliver' or fullfillment == 'Jack' or fullfillment == 'Harry' or fullfillment == 'Oscar' or fullfillment == 'James' or fullfillment == 'William' or fullfillment == 'Joe'):
            try:
                send_token = {'token' : token}
                url = requests.get("http://localhost:8000/v1/dentist/info/"+ fullfillment, params=send_token)
                available = url.json()
                return jsonify(available)
            except:
                return jsonify("The dentist system is under maintenance")

    if (intent == "Available time for Mike" or intent == "Available time for Jim" or intent == "Available time for Tracey" or intent == "Available time for Oliver" or intent == "Available time for Jack" or intent == "Available time for Harry" or intent == "Available time for Oscar" or intent == "Available time for James" or intent == "Available time for William" or intent == "Available time for Joe"):
        if (fullfillment == 'Mike' or fullfillment == 'Jim' or fullfillment == 'Tracey' or fullfillment == 'Oliver' or fullfillment == 'Jack' or fullfillment == 'Harry' or fullfillment == 'Oscar' or fullfillment == 'James' or fullfillment == 'William' or fullfillment == 'Joe'):
            try:
                send_token = {'token' : token}
                url = requests.get("http://localhost:4000/v1/dentist/timeslots/"+ fullfillment, params=send_token)
                available = url.json()
                return available
            except:
                return jsonify("The timeslot system is under maintenance")

    if (intent == "Reserve time with Mike" or intent == "Reserve time with Jim" or intent == "Reserve time with Tracey" or intent == "Reserve time with Oliver" or intent == "Reserve time with Jack" or intent == "Reserve time with Harry" or intent == "Reserve time with Oscar" or intent == "Reserve time with James" or intent == "Reserve time with William" or intent == "Reserve time with Joe"):
        if (fullfillment == 'Mike' or fullfillment == 'Jim' or fullfillment == 'Tracey' or fullfillment == 'Oliver' or fullfillment == 'Jack' or fullfillment == 'Harry' or fullfillment == 'Oscar' or fullfillment == 'James' or fullfillment == 'William' or fullfillment == 'Joe'):
            time = query.split("#", 1)[0]
            try:
                send_token = {'token' : token}
                url = requests.get("http://localhost:4000/v1/dentist/" + fullfillment +"/timeslot/" + time+ "/reserve", params=send_token)
                available = url.json()
                return available
            except:
                return jsonify("The timeslot system is under maintenance")

    if (intent == "Cancel time with Mike" or intent == "Cancel time with Jim" or intent == "Cancel time with Tracey" or intent == "Cancel time with Oliver" or intent == "Cancel time with Jack" or intent == "Cancel time with Harry" or intent == "Cancel time with Oscar" or intent == "Cancel time with James" or intent == "Cancel time with William" or intent == "Cancel time with Joe"):
        if (fullfillment == 'Mike' or fullfillment == 'Jim' or fullfillment == 'Tracey' or fullfillment == 'Oliver' or fullfillment == 'Jack' or fullfillment == 'Harry' or fullfillment == 'Oscar' or fullfillment == 'James' or fullfillment == 'William' or fullfillment == 'Joe'):
            time = query.split("~", 1)[0]
            try: 
                send_token = {'token' : token}
                url = requests.put("http://localhost:4000/v1/dentist/" + fullfillment +"/timeslot/" + time+ "/cancel", params=send_token)
                available = url.json()
                return available
            except:
                return jsonify("The timeslot system is under maintenance")


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 2000)






