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

        for i in range(self.rear, self.front - 1, -1):
            if not (self.queue[self.rear] - 3000 <= self.queue[i] <= self.queue[self.rear]):
                break
            count += 1
        
        return count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)