#!/usr/bin/env python3
"""type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """the func that return the multiplier"""
    def multiplier_func(value: float) -> float:
        """the multiplier func"""
        return value * multiplier
    return multiplier
