import asyncio

from task2.solution.domen.entities import AnimalLetterCounter
from task2.solution.infrastructure.page_cache import load_cached_links, save_links_to_cache
from task2.solution.infrastructure.wiki_collector import collect_category_page_links
from task2.solution.infrastructure.wiki_scraper import parse_all_category_pages
from task2.solution.infrastructure.file_writer import save_counts_to_csv
from task2.solution.core.logger import get_logger

logger = get_logger(__name__)

def run_beast_counter(force_refresh=False):
    logger.info("🚀 Запуск сбора животных")

    if force_refresh:
        urls = collect_category_page_links()
        save_links_to_cache(urls)
    else:
        urls = load_cached_links()
        if not urls:
            logger.info("🔁 Кэша нет, принудительный сбор")
            urls = collect_category_page_links()
            save_links_to_cache(urls)

    logger.info("⏳ Начинаем асинхронный парсинг")
    all_titles = asyncio.run(parse_all_category_pages(urls))

    counter = AnimalLetterCounter()
    for title in all_titles:
        counter.add(title)

    save_counts_to_csv(counter.result())

