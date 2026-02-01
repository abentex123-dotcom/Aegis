from dataclasses import dataclass
from pathlib import Path
import json
import os


@dataclass(frozen=True)
class AegisConfig:
    name: str = "AEGIS"
    system_prompt_path: Path = Path("prompts/system.md")
    user_prompt_path: Path = Path("prompts/user.md")
    update_config_path: Path = Path("config/update.json")
    update_url: str = ""

    @staticmethod
    def load() -> "AegisConfig":
        update_url = os.environ.get("AEGIS_UPDATE_URL", "")
        update_config_path = Path("config/update.json")
        if not update_url and update_config_path.exists():
            try:
                payload = json.loads(update_config_path.read_text(encoding="utf-8"))
                update_url = payload.get("update_url", "")
            except json.JSONDecodeError:
                update_url = ""
        return AegisConfig(update_url=update_url)
