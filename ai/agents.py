

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert 
- Local Tour Guide


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""





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
