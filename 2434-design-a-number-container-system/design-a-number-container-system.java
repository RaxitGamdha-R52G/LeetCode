class NumberContainers {
    Map<Integer, Integer> hs;
    Map<Integer, SortedSet<Integer>> container;


    public NumberContainers() {
        this.container = new HashMap<>();
        this.hs = new HashMap<>();
    }
    
    public void change(int index, int number) {
        if (hs.containsKey(index)) {
            int oldNumber = hs.get(index);
            container.get(oldNumber).remove(index);
            if (container.get(oldNumber).isEmpty()) {
                container.remove(oldNumber);
            }
        }

        hs.put(index, number);
        container.putIfAbsent(number, new TreeSet<>());
        container.get(number).add(index);
        
    }
    
    public int find(int number) {
        if(container.containsKey(number)){
            return container.get(number).first();
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