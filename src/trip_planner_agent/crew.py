from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent

from dotenv import load_dotenv
from trip_planner_agent.tools.tavily_tool import search_web

load_dotenv()


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
            verbose=True
        )

    @agent
    def researcher(self):
        return Agent(
            config=self.agents_config["researcher"],
            tools=[search_web],
            verbose=True,
            max_iter=2
        )

    @agent
    def planner(self):
        return Agent(
            config=self.agents_config["planner"],
            verbose=True
        )

    # ---------- TASKS ----------
    @task
    def intent_task(self):
        return Task(
            config=self.tasks_config["intent_task"],
            agent=self.intent_mapper()
        )

    @task
    def research_task(self):
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher()
        )

    @task
    def planning_task(self):
        return Task(
            config=self.tasks_config["planning_task"],
            agent=self.planner()
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