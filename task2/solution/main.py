import argparse
from task2.solution.application.letter_counter import run_beast_counter
from task2.solution.core.logger import setup_logger, get_logger

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Включить логирование отладки")
    parser.add_argument("--refresh", action="store_true", help="Принудительно собрать ссылки")
    args = parser.parse_args()

    setup_logger(debug=args.debug)
    logger = get_logger(__name__)

    run_beast_counter(force_refresh=args.refresh)
    logger.info("✅ Готово. Данные записаны в beasts.csv")
