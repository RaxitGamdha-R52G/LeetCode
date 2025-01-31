class RecentCounter {
    int front,rear;
    ArrayList<Integer> ar;

    public RecentCounter() {
        this.front = -1;
        this.rear = -1;
        this.ar = new ArrayList<Integer>();
        
    }
    
    public int ping(int t) {
        if(front == -1){
            front++;
        }
        rear++;
        ar.add(t);
        
        int r = ar.get(rear) - 3000;
        while (ar.get(front) < r){
            front++;
        }

        return rear + 1 - front;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */