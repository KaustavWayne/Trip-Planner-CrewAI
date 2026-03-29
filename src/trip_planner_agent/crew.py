from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent

from dotenv import load_dotenv
from trip_planner_agent.tools.tavily_tool import search_web

load_dotenv()

# from crewai import LLM

# llm = LLM(
#     model="ollama/llama3.2:3b",
#     api_base="http://localhost:11434/v1",
#     api_key="ollama"
# )

# Remove from agents.yaml if you use upper this code snippet

# ❌ Remove this:

# llm: ollama/llama3.2:3b


@CrewBase
class TravelCrew:
    """Travel Crew for AI Trip Planning"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # ✅ CrewAI automatically loads YAML
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ---------- AGENTS ----------
    @agent
    def intent_mapper(self):
        return Agent(
            config=self.agents_config["intent_mapper"],
            #llm=llm,
            verbose=True
        )

    @agent
    def researcher(self):
        return Agent(
            config=self.agents_config["researcher"],
            #llm=llm,
            tools=[search_web],
            verbose=True,
            max_iter=2
        )

    @agent
    def planner(self):
        return Agent(
            config=self.agents_config["planner"],
            #llm=llm,
            verbose=True
        )

    # ---------- TASKS ----------
    @task
    def intent_task(self):
        return Task(
            config=self.tasks_config["intent_task"]
            #agent=self.intent_mapper()
        )

    @task
    def research_task(self):
        return Task(
            config=self.tasks_config["research_task"],
            #agent=self.researcher()
            context=[self.intent_task()]
        )

    @task
    def planning_task(self):
        return Task(
            config=self.tasks_config["planning_task"],
            #agent=self.planner()
            context=[self.research_task()]
        )

    # ---------- CREW ----------
    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )


# ---------- RUN ----------
def run_crew(inputs):
    return TravelCrew().crew().kickoff(inputs=inputs)