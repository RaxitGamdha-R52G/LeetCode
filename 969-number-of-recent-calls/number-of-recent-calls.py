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

        r = self.queue[self.rear] - 3000
        while self.queue[self.front] < r:
            self.front += 1
        
        return self.rear+1 - self.front
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)