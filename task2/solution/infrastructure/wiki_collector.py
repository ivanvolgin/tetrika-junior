import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from task2.solution.core.logger import get_logger
from task2.solution.core.settings import BASE_URL, START_PAGE

logger = get_logger(__name__)

def collect_category_page_links() -> list[str]:
    urls = []
    url = urljoin(BASE_URL, START_PAGE)

    while url:
        logger.info(f"Собираем ссылки: {url}")
        urls.append(url)

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")

        next_link = soup.find("a", string="Следующая страница")
        url = urljoin(BASE_URL, next_link["href"]) if next_link else None

    logger.info(f"🔗 Всего собрано ссылок: {len(urls)}")
    return urls
