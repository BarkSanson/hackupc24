import json

from crewai import Crew
from textwrap import dedent
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request

from trip_crew import TripCrew

class TravelProposal:
    def __init__(self, departure_city, arrival_city, departure_date, return_date, interests) -> None:
        self.departure_city = departure_city
        self.arrival_city = arrival_city 
        self.departure_date = departure_date
        self.return_date = return_date
        self.interests = interests

class Recommendation:
    def __init__(self) -> None:
        self.recommendations = None
        self.relations = []
    
    def to_json(self):
        return {
            "recommendations": self.recommendations,
            "relations": self.relations
        }

    def __dict__(self):
        return {
            "recommendations": self.recommendations,
            "relations": self.relations
        }

app = Flask(__name__)

@app.route('/', methods=["POST"])
def recommendation():
    travel_proposal = request.json
    print(travel_proposal)

    departure = travel_proposal['departure_city']
    cities = travel_proposal['arrival_city']
    estimated_departure = travel_proposal['departure_date']
    return_date = travel_proposal['return_date']
    interests = travel_proposal['interests']

    trip_crew = TripCrew(departure, cities, estimated_departure, return_date, interests)
    result = trip_crew.run()

    rec = Recommendation()
    rec.recommendations = result

    return json.dumps(rec.to_json())

# This is the main function that you will use to run your custom crew.
#if __name__ == "__main__":
#    print("## Welcome to the Trip Planner Crew!")
#    print('--------------------------------------')
#    origin = input(
#        dedent("""
#        Where will you be traveling from?
#    """))
#    cities = input(
#        dedent("""Which cities are you interested in visiting?"""))
#    estimated_departure = input(
#        dedent("""What is your estimated departure date (YYYY-MM-DD)?"""))
#    estimated_arrival = input(
#        dedent("""What is your estimated arrival date (YYYY-MM-DD)?"""))
#    interests = input(
#        dedent("""What sorts of things capture your interest and keep you occupied at a higher level?"""))
#
#    trip_crew = TripCrew(origin, cities, estimated_departure, estimated_arrival, interests)
#    result = trip_crew.run()
#    print("\n\n########################")
#    print("## Here's your trip plan.")
#    print("########################\n")
#    print(result)
