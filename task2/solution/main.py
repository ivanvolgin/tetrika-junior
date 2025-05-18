from task2.solution.application.letter_counter import run_beast_counter
from task2.solution.core.logger import setup_logger, get_logger
import sys

if __name__ == "__main__":
    debug = "--debug" in sys.argv
    setup_logger(debug=debug)
    logger = get_logger(__name__)

    run_beast_counter()
    logger.info("✅ Готово. Данные записаны в beasts.csv")