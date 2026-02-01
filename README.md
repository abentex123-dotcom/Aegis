# AEGIS Assistant Shell

Minimal, extensible shell for the AEGIS AI assistant. This repository provides a
clean project scaffold with configuration, prompt templates, and a runnable CLI
stub that can be connected to any LLM backend.

## Features

- Structured configuration (`config/`)
- Prompt templates (`prompts/`)
- Extendable Python package (`aegis/`)
- Simple CLI entry point for local testing
- Russian-only responses enforced via system prompt
- Installer scripts for one-click local запуск on Windows/macOS/Linux
- Optional update checks via update manifest URL

## Quick start

```bash
python -m aegis.cli --message "Привет, AEGIS!"
```

## One-click installer

Скачайте репозиторий и запустите установщик:

- Windows: `installers/AEGIS-Installer.bat`
- macOS/Linux: `installers/AEGIS-Installer.sh`

## Обновления

Чтобы ассистент проверял обновления при запуске, укажите URL манифеста:

- Переменная окружения `AEGIS_UPDATE_URL`
- Либо поле `update_url` в `config/update.json`

Формат манифеста:

```json
{
  "version": "0.1.2",
  "download_url": "https://example.com/AEGIS-Installer"
}
```

## Project layout

```
.
├── aegis/               # Core assistant logic
├── config/              # Environment-independent configuration
├── prompts/             # System/user prompt templates
└── scripts/             # Helper scripts (optional)
```

## Next steps

- Plug in your LLM provider in `aegis/llm.py`.
- Extend routing/policies in `aegis/policies.py`.
- Add tools and skills under `aegis/tools/`.
