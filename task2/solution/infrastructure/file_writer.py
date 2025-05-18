import csv
from task2.solution.core.logger import get_logger

logger = get_logger(__name__)


def save_counts_to_csv(counts: dict, filename: str = "task2/beasts.csv"):
    logger.info(f"Сохраняем данные в файл: {filename}")
    with open(filename, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for letter in sorted(counts):
            writer.writerow([letter, counts[letter]])
            logger.debug(f"{letter},{counts[letter]}")
