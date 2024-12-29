# Agenticrag Crew

Welcome to the Agenticrag Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/agenticrag/config/agents.yaml` to define your agents
- Modify `src/agenticrag/config/tasks.yaml` to define your tasks
- Modify `src/agenticrag/crew.py` to add your own logic, tools and specific args
- Modify `src/agenticrag/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the AgenticRAG Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The AgenticRAG Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Agenticrag Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

## About the Maintainer

This instance of the Agenticrag Crew project is actively maintained by Mustaq Sohail Shaik. With over 4 years of professional experience, Mustaq specializes in Data Engineering and AI-driven system design, including building scalable data pipelines and integrating LLMs with enterprise systems. His expertise spans agent frameworks like CrewAI, RAG, and cloud-native deployments.

For questions or contributions related to this specific project implementation, feel free to connect:

-   **GitHub:** [Git-Repo](https://github.com/Git-Repo)
-   **LinkedIn:** [Mustaq Sohail Shaik](https://linkedin.com/in/adarsh-umesh)
-   **Email:** reachtomustaqsohail@gmail.com