#!/usr/bin/env python3
"""Annotate the below function’s parameters and return
values with the appropriate types"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """the func with appropiate types"""
    return [(i, len(i)) for i in lst]
