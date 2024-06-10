#!/usr/bin/env python3
"""function"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay) -> float:
    """calculate time taken to execute n tasks and return the average time"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n


print(measure_time(5, 9))