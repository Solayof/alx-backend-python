#!/usr/bin/env python3
"""measure the runtime of four concurrent async_comprehension function"""
import asyncio
from time import time 
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function that compute runtime of four parallel async_compresion"""
    start: float = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
