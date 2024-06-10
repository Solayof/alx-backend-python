#!/usr/bin/env python3
"""function that take max_delay and return asynio.task"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create an instance of wait_random and ruturn the task
    """
    return asyncio.create_task(wait_random(max_delay))
