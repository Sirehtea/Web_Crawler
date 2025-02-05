import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
import json
from urllib.parse import urljoin

print("bv: \"https://www.google.com/\"")
URL = input("Website die je wilt doorzoeken: ")
DIEPTE = input("Kies de maximale diepte")

class WordCounter:
    def __init__(self):
        self.word_counts = {}

    def count_word(self, word):
        self.word_counts[word] = self.word_counts.get(word, 0) + 1

async def fetch_html(url, base_url=URL):
    full_url = urljoin(base_url, url)

    async with aiohttp.ClientSession() as session:
        async with session.get(full_url) as response:
            return await response.text()

async def extract_content(html, word_counter):
    soup = BeautifulSoup(html, 'html.parser')
    text_content = soup.get_text()
    words = re.findall(r'\b\w+\b', text_content)

    for word in words:
        word_counter.count_word(word)

    links = [a['href'] for a in soup.find_all('a', href=True)]

    return links

class Crawler:
    def __init__(self, visited, initial_page, max_depth, word_counter):
        self.max_depth = max_depth
        self.initial_page = initial_page
        self.visited = visited
        self.word_counter = word_counter
        self.background_tasks = set()

    async def crawl(self, starting_link, depth):
        if depth == 0 or starting_link in self.visited:
            return

        self.visited.add(starting_link)
        html_code = await fetch_html(starting_link)

        links = await extract_content(html_code, self.word_counter)

        for link in links:
            task = asyncio.create_task(self.crawl(link, depth - 1))
            self.background_tasks.add(task)
            task.add_done_callback(self.background_tasks.discard)

async def async_main():
    start_url = URL

    word_counter = WordCounter()
    crawler = Crawler(set(), start_url, DIEPTE, word_counter)

    await crawler.crawl(start_url, 2)

    while crawler.background_tasks:
        await asyncio.gather(*crawler.background_tasks)

    total_count = sum(word_counter.word_counts.values())

    result = {
        "total": total_count,
        "counts": word_counter.word_counts
    }

    try:
        with open("output.json", 'w') as json_file:
            json.dump(result, json_file, indent=2)
        print("Data weggeschreven naar \"output.json\".")
    except Exception as e:
        print("Data wegschrijven naar \"output.json\" mislukt.")

if __name__ == "__main__":
    asyncio.run(async_main())
