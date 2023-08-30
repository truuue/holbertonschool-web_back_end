#!/usr/bin/env python3
"""coroutine will collect 10 random numbers using
an async comprehensing over async_generator"""
async_generator = __import__('0-async_generator').async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async"""
    return (_ async for _ in async_generator())
