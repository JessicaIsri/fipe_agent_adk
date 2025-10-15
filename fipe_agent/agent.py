import logging
from typing import AsyncGenerator

from google.adk.agents import LlmAgent, BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from typing_extensions import override

from fipe_agent.consulta_marcas.agent import consulta_marcas
from fipe_agent.consulta_modelo.agent import consulta_modelos
from fipe_agent.consulta_ano.agent import consulta_anos
from fipe_agent.consulta_fipe.agent import consulta_fipe


from fipe_agent.openapi_spec.openapi_file_spec import openapi_spec_string

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OrchestratorAgent(BaseAgent):
    consulta_marcas: LlmAgent
    consulta_modelos: LlmAgent
    consulta_anos: LlmAgent
    consulta_fipe: LlmAgent


    def __init__(self,
                 name: str,
                 consulta_marcas: LlmAgent,
                 consulta_modelos: LlmAgent,
                 consulta_anos: LlmAgent,
                 consulta_fipe: LlmAgent):
        super().__init__(
            name=name,
            consulta_marcas=consulta_marcas,
            consulta_modelos=consulta_modelos,
            consulta_anos=consulta_anos,
            consulta_fipe=consulta_fipe,
            description="Esse é o orquestrador para a consulta da tabela FIPE"
        )

    @override
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        async for event in self.consulta_marcas.run_async(ctx):
            logger.info(f"[{self.name}] - {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event

        consulta_marcas_output = ""
        if "consulta_marcas_output" in ctx.session.state:
            consulta_marcas_output = ctx.session.state['consulta_marcas_output']
            logger.info(f"[{self.name}] - {consulta_marcas_output}")

        consulta_modelos_output = ""
        if "consulta_modelos_output" in ctx.session.state:
            consulta_modelos_output = ctx.session.state['consulta_modelos_output']
            logger.info(f"[{self.name}] - {consulta_modelos_output}")

        consulta_anos_output = ""
        if "consulta_anos_output" in ctx.session.state:
            consulta_anos_output = ctx.session.state['consulta_anos_output']
            logger.info(f"[{self.name}] - {consulta_anos_output}")

        conslta_fipe_output = ""
        if "conslta_fipe_output" in ctx.session.state:
            conslta_fipe_output = ctx.session.state['conslta_fipe_output']
            logger.info(f"[{self.name}] - {conslta_fipe_output}")

        analise_condicao_veiculo_output = ""
        if "analise_condicao_veiculo_output" in ctx.session.state:
            analise_condicao_veiculo_output = ctx.session.state['analise_condicao_veiculo_output']
            logger.info(f"[{self.name}] - {analise_condicao_veiculo_output}")

orchestrator_agent = OrchestratorAgent(
    name="consultor_fipe",
    consulta_marcas=consulta_marcas,
    consulta_modelos=consulta_modelos,
    consulta_anos=consulta_anos,
    consulta_fipe=consulta_fipe
)

root_agent = orchestrator_agent