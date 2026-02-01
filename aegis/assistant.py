from aegis.config import AegisConfig
from aegis.llm import LlmClient
from aegis.policies import ResponsePolicy
from aegis.prompts import PromptLoader


class AegisAssistant:
    """Core assistant orchestration shell."""

    def __init__(
        self,
        config: AegisConfig | None = None,
        llm_client: LlmClient | None = None,
        policy: ResponsePolicy | None = None,
    ) -> None:
        self.config = config or AegisConfig()
        self.prompts = PromptLoader(self.config)
        self.llm = llm_client or LlmClient()
        self.policy = policy or ResponsePolicy()

    def respond(self, message: str) -> str:
        system_prompt = self.prompts.load_system_prompt()
        user_prompt = self.prompts.load_user_prompt(message)
        raw = self.llm.generate(system_prompt, user_prompt)
        return self.policy.apply(raw)
