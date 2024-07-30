class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        max_freq = max(freq)
        return (max_freq-1) * n - (sum(freq)-max_freq-(freq.count(max_freq)-1)) + len(tasks) if (max_freq-1) * n - (sum(freq)-max_freq-(freq.count(max_freq)-1)) > 0 else len(tasks)