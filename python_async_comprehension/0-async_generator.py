#!/usr/bin/env python3
"""coroutine will loop 10 times, each time asynchronously wait 1 second"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """random number between 0 and 10 func"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
