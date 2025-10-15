from google.adk import Agent
from pydantic import BaseModel, Field

from fipe_agent.consulta_marcas import prompt
from fipe_agent.consulta_modelo.agent import consulta_modelos
from fipe_agent.openapi_spec.openapi_file_spec import fipe_toolset

MODEL = "gemini-2.0-flash"


consulta_marcas = Agent(
model=MODEL,
name="consulta_marcas",
instruction=prompt.consulta_marcas,
tools=[fipe_toolset],
output_key='consulta_marcas_output'
)