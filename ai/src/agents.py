from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

class TravelAgents:
    def __init__(self):
        # Correctly specifying the model name for GPT-4
        self.OpenAIGPT4 = ChatOpenAI(
            model_name="gpt-4", temperature=0.7)

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                """Expert in travel planning and logistics. 
                I have decades of experience making travel itineraries."""),
            goal=dedent("""
                        Create a 7-day travel itinerary with detailed per-day plans,
                        including budget, packing suggestions, and safety tips.
                        """),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate
            ],
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
                """Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(
                """Select the best cities based on weather, season, prices, and traveler interests"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(
                """Knowledgeable local guide with extensive information
                about the city, its attractions, and customs"""),
            goal=dedent(
                """Provide the BEST insights about the selected city"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT4,
        )
    
    #def budget_planner(self):
        #return Agent(
            #role="Budget Planner",
            #backstory=dedent(
                #"""Specialist in creating travel budgets and finding cost-saving measures for trips."""),
            #goal=dedent("""
                        #Develop a comprehensive budget plan covering flights, accommodation, 
                        #food, local transportation, and activities for the entire trip.
                        #"""),
            #tools=[CalculatorTools.calculate, SearchTools.search_internet],
            #verbose=True,
            #llm=self.OpenAIGPT4,
        #)

    #def cultural_enthusiast(self):
        #return Agent(
            #role="Cultural Enthusiast",
            #backstory=dedent(
                #"""Passionate about local culture and history, providing insights into customs and festivals."""),
            #goal=dedent("""
                        #Offer detailed information on local customs, historical sites, and festivals 
                        #to enrich travelers' understanding and enjoyment.
                        #"""),
            #tools=[SearchTools.search_internet],
            #verbose=True,
            #llm=self.OpenAIGPT4,
        #)

    #def transportation_coordinator(self):
        #return Agent(
            #role="Transportation Coordinator",
            #backstory=dedent(
                #"""Experienced in optimizing travel routes and finding convenient transportation options."""),
            #goal=dedent("""
                        #Create an optimized travel route, including flights, local transportation, 
                        #and transfers between destinations.
                        #"""),
            #tools=[SearchTools.search_internet],
            #verbose=True,
            #llm=self.OpenAIGPT4,
        #)

