#!/usr/bin/env python3
"""random waiting module"""

import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """wait for a random number"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
