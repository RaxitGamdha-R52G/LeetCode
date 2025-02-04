class BrowserHistory {
    ListNode head;
    ListNode curr;

    public BrowserHistory(String homepage) {
        this.head = new ListNode(homepage);
        this.curr = head;
    }
    
    public void visit(String url) {
        ListNode temp = this.curr;
        ListNode n = new ListNode(url);
        temp.next = n;
        n.prev = temp;
        this.curr = n;
    }
    
    public String back(int steps) {
        String result = this.curr.val;
        int count = 0;
        ListNode temp = this.curr;
        while(count < steps && temp.prev != null){
            temp = temp.prev;
            result = temp.val;
            count++;
        }

        this.curr = temp;
        return result;
    }
    
    public String forward(int steps) {
        String result = this.curr.val;
        int count = 0;
        ListNode temp = this.curr;
        while(count < steps && temp.next != null){
            temp = temp.next;
            result = temp.val;
            count++;
        }
        this.curr = temp;
        return result;
    }
}

class ListNode{
    String val;
    ListNode next;
    ListNode prev;

    public ListNode(String val){
        this.val = val;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */