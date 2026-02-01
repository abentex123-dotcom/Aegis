from aegis.config import AegisConfig


class PromptLoader:
    def __init__(self, config: AegisConfig) -> None:
        self.config = config

    def load_system_prompt(self) -> str:
        return self._read_or_default(
            self.config.system_prompt_path,
            (
                "Ты AEGIS, ассистент с безопасными и точными ответами. "
                "Всегда отвечай только на русском языке."
            ),
        )

    def load_user_prompt(self, message: str) -> str:
        template = self._read_or_default(
            self.config.user_prompt_path,
            "Пользователь: {message}",
        )
        return template.format(message=message)

    @staticmethod
    def _read_or_default(path, fallback: str) -> str:
        try:
            return path.read_text(encoding="utf-8").strip()
        except FileNotFoundError:
            return fallback
