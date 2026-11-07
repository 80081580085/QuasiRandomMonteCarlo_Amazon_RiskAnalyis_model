"""Utility functions for the risk analysis code."""

from functools import wraps
import time


def timeit(func):
  """A decorator that measures runtime of a function."""

  @wraps(func)
  def wrapper(*args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    print(f"[{func.__name__}] finished in {end - start:.4f} seconds")
    return result

  return wrapper
