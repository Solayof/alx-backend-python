#!/usr/bin/env python3
"""spawn task_wait_random n times"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay) -> List[float]:
    """execute wait_random n times"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in  asyncio.as_completed(tasks)]


print(asyncio.run(task_wait_n(4, 8)))