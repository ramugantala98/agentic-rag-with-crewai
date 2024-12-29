from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool
from agenticrag.tools.custom_tool import GenerationTool,SearchTool
import os
from dotenv import load_dotenv

load_dotenv()

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


config = dict(
    llm=dict(
        provider="azure_openai",
        config=dict(
            model="gpt-4o"
        ),
    ),
    embedder=dict(
        provider="azure_openai",
        config=dict(
            model="text-embedding-3-small"
        ),
    ),
)

pdf_search_tool = PDFSearchTool(config=config,pdf='my.pdf')



generation_tool=GenerationTool()
web_search_tool = SearchTool()

@CrewBase
class Agenticrag():
	"""Agenticrag crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def router_Agent(self) -> Agent:
		return Agent(
			config=self.agents_config['router_Agent'],
			verbose=True
		)

	@agent
	def retriever_Agent(self) -> Agent:
		return Agent(
			config=self.agents_config['retriever_Agent'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def router_task(self) -> Task:
		return Task(
			config=self.tasks_config['router_task'],
		)

	@task
	def retriever_task (self) -> Task:
		return Task(
			config=self.tasks_config['retriever_task'],
			output_file='report.md',
			tools=[generation_tool,web_search_tool,pdf_search_tool]
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Agenticrag crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
