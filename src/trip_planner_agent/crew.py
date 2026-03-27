from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent

from dotenv import load_dotenv
from pathlib import Path
import yaml

from trip_planner_agent.tools.tavily_tool import search_web

load_dotenv()

# 🔥 ABSOLUTE SAFE PATH
BASE_PATH = Path(__file__).resolve().parent


# ---------- SAFE YAML LOADER ----------
def load_yaml(path):
    print(f"\n🔍 Loading YAML from: {path}")

    if not path.exists():
        raise FileNotFoundError(f"❌ File NOT FOUND: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if data is None:
        raise ValueError(f"❌ YAML EMPTY OR INVALID: {path}")

    print(f"✅ Loaded keys: {list(data.keys())}\n")

    return data


@CrewBase
class TravelCrew:

    agents: list[BaseAgent]
    tasks: list[Task]

    def __init__(self, inputs):
        self.inputs = inputs

        # 🔥 FORCE CORRECT PATH
        agents_path = BASE_PATH / "config" / "agents.yaml"
        tasks_path = BASE_PATH / "config" / "tasks.yaml"

        self.agents_config = load_yaml(agents_path)
        self.tasks_config = load_yaml(tasks_path)

    # ---------- AGENTS ----------
    @agent
    def intent_mapper(self):
        return Agent(
            config=self.agents_config.get("intent_mapper"),
            verbose=True
        )

    @agent
    def researcher(self):
        return Agent(
            config=self.agents_config.get("researcher"),
            tools=[search_web],
            verbose=True,
            max_iter=2
        )

    @agent
    def planner(self):
        return Agent(
            config=self.agents_config.get("planner"),
            verbose=True
        )

    # ---------- TASKS ----------
    @task
    def intent_task(self):
        config = self.tasks_config.get("intent_task")
        if not config:
            raise ValueError("❌ intent_task missing in tasks.yaml")

        return Task(
            config=config,
            agent=self.intent_mapper()
        )

    @task
    def research_task(self):
        config = self.tasks_config.get("research_task")
        if not config:
            raise ValueError("❌ research_task missing in tasks.yaml")

        return Task(
            config=config,
            agent=self.researcher()
        )

    @task
    def planning_task(self):
        config = self.tasks_config.get("planning_task")
        if not config:
            raise ValueError("❌ planning_task missing in tasks.yaml")

        return Task(
            config=config,
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
    return TravelCrew(inputs).crew().kickoff(inputs=inputs)