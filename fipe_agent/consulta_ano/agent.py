from google.adk import Agent
from pydantic import BaseModel, Field

from fipe_agent.consulta_ano.prompt import consulta_anos_instruction
from fipe_agent.openapi_spec.openapi_file_spec import fipe_toolset

MODEL = "gemini-2.0-flash"


consulta_anos = Agent(
model=MODEL,
name="consulta_modelo",
instruction=consulta_anos_instruction,
tools=[fipe_toolset],
output_key='consulta_anos_output'
)