class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        max_freq,temp = max(freq),(sum(freq)-max(freq)-(freq.count(max(freq))-1))
        return (max_freq-1) * n - temp + len(tasks) if (max_freq-1) * n - temp > 0 else len(tasks)