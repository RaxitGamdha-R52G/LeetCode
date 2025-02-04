class MyHashSet {
    ListNode head;
    ListNode tail;

    public MyHashSet() {        
        this.head = new ListNode(0); // Dummy Node
        this.tail = this.head;
    }
    
    public void add(int key) {
        if(contains(key)){
            return;
        }
        tail.next = new ListNode(key);
        tail = tail.next;
        return;
    }
    
    public void remove(int key) {
        ListNode prev = head, curr = head.next;
        while(curr != null){
            if(curr.key == key){
                prev.next = curr.next;
                if (curr == tail) {
                    tail = prev; 
                }
                return;
            }
            prev = curr;
            curr = curr.next;
        }

        return;
    }
    
    public boolean contains(int key) {
        ListNode curr = head.next;
        while(curr != null){
            if(curr.key == key){
                return true;
            }
            curr = curr.next;
        }

        return false;
    }
}

class ListNode{
    int key;
    ListNode next;

    public ListNode(int key){
        this.key = key;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */