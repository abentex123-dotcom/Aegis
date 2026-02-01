import argparse

from aegis.assistant import AegisAssistant
from aegis.config import AegisConfig
from aegis.updater import check_for_updates


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AEGIS assistant shell CLI.")
    parser.add_argument(
        "--message",
        "-m",
        default="Привет!",
        help="User message to send into the shell.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    config = AegisConfig.load()
    update_message = check_for_updates(config.update_url)
    if update_message:
        print(update_message)
    assistant = AegisAssistant(config=config)
    print(assistant.respond(args.message))


if __name__ == "__main__":
    main()
