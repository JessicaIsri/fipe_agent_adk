from google.adk import Agent
from pydantic import BaseModel, Field

from fipe_agent.consulta_modelo import prompt
from fipe_agent.openapi_spec.openapi_file_spec import fipe_toolset

MODEL = "gemini-2.0-flash"

consulta_modelos = Agent(
model=MODEL,
name="consulta_modelo",
instruction=prompt.consulta_modelos_instruction,
tools=[fipe_toolset],
output_key='consulta_modelos_output'
)