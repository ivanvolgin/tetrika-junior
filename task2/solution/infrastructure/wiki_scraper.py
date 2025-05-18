import aiohttp
from bs4 import BeautifulSoup
from task2.solution.core.logger import get_logger

logger = get_logger(__name__)

def is_valid_title(title: str) -> bool:
    title = title.strip()
    if not title:
        return False
    if ":" in title:  # фильтруем роды и подкатегории
        return False
    if not title[0].isalpha():  # пропускаем всё, что не начинается с буквы
        return False
    return True

async def fetch_and_extract_titles(session: aiohttp.ClientSession, url: str) -> list[str]:
    async with session.get(url) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, "html.parser")
        raw_titles = [li.get_text(strip=True) for li in soup.select(".mw-category li")]
        titles = [title for title in raw_titles if is_valid_title(title)]
        logger.debug(f"[ASYNC] {url} → {len(titles)} / {len(raw_titles)} записей после фильтрации")
        return titles

async def parse_all_category_pages(urls: list[str]) -> list[str]:
    import asyncio
    all_titles = []

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_extract_titles(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for titles in results:
        all_titles.extend(titles)

    logger.info(f"📄 Обработано страниц: {len(results)}, всего записей: {len(all_titles)}")
    return all_titles
