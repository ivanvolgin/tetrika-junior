from collections import defaultdict
from task2.solution.core.logger import get_logger
import re

logger = get_logger(__name__)


class AnimalLetterCounter:
    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, title: str):
        if not title:
            return

        stripped = title.strip()
        if not stripped:
            return

        first_letter = stripped[0].upper()
        if re.match(r"[A-ZА-ЯЁ]", first_letter):
            self.counts[first_letter] += 1
        else:
            self.counts["?"] += 1
            logger.debug(f"⚠️ Неизвестный символ: {repr(first_letter)} в заголовке: {title}")

    def result(self):
        return dict(self.counts)
