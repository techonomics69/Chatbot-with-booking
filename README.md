# Chatbot-with-booking
COMP9322 ASS1
Note: Please do run Dentist service and timeslots service in the respective docker container because
paths have been set up.

Dialogflow service:
Go to dialogflow folder:
Type the following command in the terminal:
pip install -r requirements.txt python dialogflow.py

Dentist service:
In the dentist folder, go to app folder, there is a Dockerfile.
Type the following commands in the terminal:
docker build -t dentist .
docker run -p 8000:8000 -it dentist

Timeslots service:
In the timeslot folder, go to app folder, there is a Dockerfile.
Type the following commands in the terminal:
docker build -t timeslot .
docker run -p 4000:4000 -it timeslot

Frontend service:
Go to frontend folder:
Type the following commands in the terminal:
npm install npm start

Then go to http://localhost:3000/. The username is 1234. The password is admin.
