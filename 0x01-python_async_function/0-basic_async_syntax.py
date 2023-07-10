#!/usr/bin/env python3
"""Contains a coroutine that delays a certain amount of time and returns it"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Wait for some time"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
