class NumberContainers {
    Map<Integer, Integer> hs;
    Map<Integer, PriorityQueue<Integer>> container;


    public NumberContainers() {
        this.container = new HashMap<>();
        this.hs = new HashMap<>();
    }
    
    public void change(int index, int number) {
        if (hs.containsKey(index)) {
            int oldNumber = hs.get(index);
            if(oldNumber == number) return;

            container.get(oldNumber).remove(index);
            if (container.get(oldNumber).isEmpty()) {
                container.remove(oldNumber);
            }
        }

        hs.put(index, number);
        container.computeIfAbsent(number, k -> new PriorityQueue<>()).offer(index);
        // if(!container.containsKey(number)){
        //     container.put(number, new PriorityQueue<>());
        // }
        // // container.putIfAbsent(number, new PriorityQueue<>());
        // container.get(number).offer(index);
        
    }
    
    public int find(int number) {
        if(container.containsKey(number)){
            return container.get(number).peek();
        }else{
            return -1;
        }
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */