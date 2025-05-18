import json
import os
from task2.solution.core.logger import get_logger
from task2.solution.core.settings import CACHE_FILE

logger = get_logger(__name__)

def load_cached_links() -> list[str]:
    if not os.path.exists(CACHE_FILE):
        logger.warning("⚠️ Кэш ссылок не найден")
        return []
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        links = json.load(f)
    logger.info(f"📂 Загружено ссылок из кэша: {len(links)}")
    return links

def save_links_to_cache(links: list[str]) -> None:
    os.makedirs("data", exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(links, f, ensure_ascii=False, indent=2)
    logger.info(f"💾 Ссылки сохранены в {CACHE_FILE}")
