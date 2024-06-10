#!/usr/bin/env python3
"""spawn wait_random n times"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


await def wait_n(n, max_delay) -> List[float]:
    """execute wait_random n times"""
    tasks = [asyncio.create_task(wait_random) for _ in range(n)]
    return [await task for task in  asyncio.as_completed(tasks)]
