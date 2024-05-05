from crewai import Crew

from agents import TravelAgents
from tasks import TravelTasks

class TripCrew:
    def __init__(self, origin, cities, estimated_departure, estimated_arrival, interests):
        self.origin = origin
        self.cities = cities
        self.estimated_departure = estimated_departure
        self.estimated_arrival = estimated_arrival
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()
        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()
        # Custom tasks include agent name and variables as input

        #budget_planner = agents.budget_planner()
        #cultural_enthusiast = agents.cultural_enthusiast()
        #transportation_coordinator = agents.transportation_coordinator()

        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.estimated_departure,
            self.estimated_arrival,
            self.interests  # Ensure this argument is passed
        )
        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,  # Pass interests to this function as well
            self.estimated_departure,
            self.estimated_arrival
        )
        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.estimated_departure,
            self.estimated_arrival,
            self.interests  # Include interests here too
        )

        #create_budget_plan = tasks.create_budget_plan(
            #budget_planner,
            #self.cities,
            #self.estimated_departure,
            #self.estimated_arrival,
            #self.interests
        #)

        #explore_culture = tasks.explore_culture(
            #cultural_enthusiast,
            #self.cities,
            #self.interests
        #)

        #plan_transportation = tasks.plan_transportation(
            #transportation_coordinator,
            #self.cities,
            #self.estimated_departure,
            #self.estimated_arrival
        #)

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent,
                    city_selection_expert,
                    local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        # Assemble the crew
        #crew = Crew(
            #agents=[
                #expert_travel_agent, city_selection_expert, local_tour_guide,
                #budget_planner, cultural_enthusiast, transportation_coordinator
            #],
            #tasks=[plan_itinerary, identify_city, gather_city_info, create_budget_plan, explore_culture, plan_transportation],
            #verbose=True,
        #)

        result = crew.kickoff()
        return result