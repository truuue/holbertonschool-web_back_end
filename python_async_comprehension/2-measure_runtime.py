#!/usr/bin/env python3
"""coroutine that will execute async_comprehension
four times in parallel using asyncio.gather"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it"""
    start_time = time.time()
    coroutines_list = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines_list)
    end_time = time.time()

    return end_time - start_time
