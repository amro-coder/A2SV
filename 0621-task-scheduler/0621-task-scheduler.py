class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        return (max(freq)-1) * n - (sum(freq)-max(freq)-(freq.count(max(freq))-1)) + len(tasks) if (max(freq)-1) * n - (sum(freq)-max(freq)-(freq.count(max(freq))-1)) > 0 else len(tasks)