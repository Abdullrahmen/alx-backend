#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return start index and an end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)