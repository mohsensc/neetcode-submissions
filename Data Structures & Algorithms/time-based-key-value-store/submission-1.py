from bisect import bisect_right
from collections import defaultdict as dd

class TimeMap:

    def __init__(self):
        self.times = dd(list)
        self.values = dd(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.times:
            return ""

        i = bisect_right(self.times[key], timestamp)

        return self.values[key][i-1] if i else ""
