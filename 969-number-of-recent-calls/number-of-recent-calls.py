class RecentCounter:

    def __init__(self):
        self.front = -1
        self.rear = -1
        self.queue = []

    def ping(self, t: int) -> int:
        if self.front == -1:
            self.front += 1
        self.queue.append(t)
        self.rear += 1
        count = 0

        r = self.queue[self.rear] - 3000
        i = self.rear
        while i >= self.front:
            if not (r <= self.queue[i]):
                break
            count += 1
            i -= 1
        
        return count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)