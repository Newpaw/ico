import aiohttp
import asyncio
import logging

from typing import List, Optional

from .json_parser import parse_company_data
from .models import Company


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

def validation_ico(ico: str) -> bool:
    """
    Validates a Czech ICO (business identifier).
    
    Args:
    ico (str): The ICO number to validate.
    
    Returns:
    bool: True if the ICO is valid, False otherwise.
    """
    if len(ico) != 8 or not ico.isdigit():
        return False
    weights = [8, 7, 6, 5, 4, 3, 2]
    weighted_sum = sum(int(ico[i]) * weights[i] for i in range(7))
    check_digit = (11 - weighted_sum % 11) % 10
    return check_digit == int(ico[7])


async def fetch_business_data(session: aiohttp.ClientSession, ico: str) -> Optional[Company]:
    """
    Asynchronously fetches business data for a given ICO.
    ...
    """
    if not validation_ico(ico):
        return None

    try:
        url = f'https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}'
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            return parse_company_data(data)
    except aiohttp.ClientError as e:
        logger.error(f"Error communicating with API: {e}")
    except asyncio.TimeoutError:
        logger.error("Timeout occurred while communicating with API.")
    except Exception as e:
        logger.error(f"General error: {e}")
    return None


async def async_fetch_company_data_by_ico(ico: str) -> Optional[Company]:
    """
    Asynchronously fetches business data for a single Czech ICO. This function
    should be called within an async context.

    Args:
    ico (str): The ICO number to fetch data for.

    Returns:
    Optional[Company]: A Company object if data is successfully fetched and parsed, None otherwise.
    """
    async with aiohttp.ClientSession() as session:
        return await fetch_business_data(session, ico)

def fetch_company_data_by_ico(ico: str) -> Optional[Company]:
    """
    Synchronously fetches business data for a single Czech ICO.

    Args:
    ico (str): The ICO number to fetch data for.

    Returns:
    Optional[Company]: A Company object if data is successfully fetched and parsed, None otherwise.
    """
    return asyncio.run(async_fetch_company_data_by_ico(ico))



async def fetch_companies_data_by_icos(icos: List[str], max_concurrent_requests: int = 5) -> List[Optional[Company]]:
    """
    Asynchronously fetches business data for a list of Czech ICOs with a limit on concurrent requests.

    Args:
    icos (List[str]): A list of ICO numbers to fetch data for.
    max_concurrent_requests (int): Maximum number of concurrent requests.

    Returns:
    List[Optional[Company]]: A list of Company objects or None for each ICO in case of failed retrieval or validation.
    """
    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(max_concurrent_requests)
        tasks = [fetch_business_data_with_semaphore(session, semaphore, ico) for ico in icos]
        return await asyncio.gather(*tasks)

async def fetch_business_data_with_semaphore(session: aiohttp.ClientSession, semaphore: asyncio.Semaphore, ico: str) -> Optional[Company]:
    """
    Fetches business data for a given ICO, using a semaphore to limit concurrent requests.

    Args:
    session (aiohttp.ClientSession): The HTTP session to use for requests.
    semaphore (asyncio.Semaphore): Semaphore to limit concurrent requests.
    ico (str): The ICO number for which to fetch data.

    Returns:
    Optional[Company]: A Company object if data is successfully fetched and parsed, None if validation fails.
    """
    async with semaphore:
        return await fetch_business_data(session, ico)



if __name__ == "__main__":
    pass