#!/usr/bin/env python3
"""function should return a float"""
wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """the measure time func"""
    async def async_measure():
        """the async measure timer"""
        start_time = time.time()
        await wait_n(n, max_delay)
        end_time = time.time()
        total_time = end_time - start_time
        return total_time / n
    
    return asyncio.run(async_measure())
