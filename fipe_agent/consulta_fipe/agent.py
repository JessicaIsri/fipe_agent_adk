from google.adk import Agent

from fipe_agent.consulta_fipe import prompt
from fipe_agent.openapi_spec.openapi_file_spec import fipe_toolset

MODEL = "gemini-2.0-flash"

consulta_fipe = Agent(
model=MODEL,
name="consulta_fipe",
instruction=prompt.consulta_fipe_instruction,
tools=[fipe_toolset],
output_key='consulta_fipe_output'
)