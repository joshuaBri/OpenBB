"""Government US Helpers."""
from typing import Any

from openbb_core.provider.utils.helpers import amake_request
from random_user_agent.user_agent import UserAgent


def get_random_agent() -> str:
    """Generate a random user agent for a request."""
    user_agent_rotator = UserAgent(limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent


async def response_callback(response, _):
    """Use callback for HTTP Client Response."""
    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        return await response.json()
    if "text" in content_type:
        return await response.text()
    return await response.read()


async def treasury_auction(url, use_cache: bool = True, **kwargs) -> Any:
    """Use the generic nasdaq HTTP request."""
    # pylint: disable=import-outside-toplevel
    from aiohttp_client_cache import SQLiteBackend
    from aiohttp_client_cache.session import CachedSession
    from openbb_core.app.utils import get_user_cache_directory
    cache_dir = get_user_cache_directory()
    backend = SQLiteBackend(
        f"{cache_dir}/http/government_us_directories", expire_after=3600 * 24
    )
    data: Any = None
    if use_cache is True:
        async with CachedSession(cache=backend) as cached_session:
            try:
                response = await cached_session.get(url, timeout=10, **kwargs)
                data = await response_callback(response, None)
            finally:
                await cached_session.close()
    else:
        data = await amake_request(url)
    return data
