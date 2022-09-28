import asyncio
import aiohttp
import logging

from rest_framework import status

logger = logging.getLogger(__name__)


async def parse_data(article):
    url = f"https://wbx-content-v2.wbstatic.net/ru/{article}.json"

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == status.HTTP_200_OK:
                    result = await response.json()
                    return {
                        'article': article,
                        'brand': result.get('selling').get('brand_name'),
                        'title': result.get('imt_name'),
                    }
                else:
                    logger.info(f'Article {article} not found.')
                    return {
                        'article': article,
                        'brand': "Not found",
                        'title': "Not found",
                    }
        except aiohttp.ClientError as error:
            logger.error(f'Error with ClientSession: {error}.')


def run_tasks(articles):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    tasks = []
    for article in articles:
        task = parse_data(article)
        tasks.append(task)

    result = loop.run_until_complete(asyncio.gather(*tasks))

    return result


