import asyncio

import aiohttp
from bs4 import BeautifulSoup

from core import async_session
from models import Anime


async def main():
    session = async_session()
    base_url = "https://shikimori.me/animes"

    async with aiohttp.ClientSession() as client_session:
        async with client_session.get(base_url) as resp:
            contents = await resp.read()

    soup = BeautifulSoup(contents, "html.parser")
    anime_list = soup.find_all("article", {"class": "b-catalog_entry"})

    for anime in anime_list:
        poster_link = anime.find("img")["src"]
        title = anime.find("span", {"class": "name-ru"}).get_text()
        publishing_year, type_ = (
            misc_tag.get_text()
            for misc_tag in anime.find("span", {"class": "misc"}).find_all("span")
        )
        session.add(
            Anime(
                title=title,
                type_=type_,
                publishing_year=int(publishing_year),
                poster_link=poster_link,
            )
        )

    await session.commit()
    await session.close()


if __name__ == "__main__":
    asyncio.run(main())
