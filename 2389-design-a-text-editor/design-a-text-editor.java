class TextEditor {
    Node head;
    Node pos;
    public TextEditor() {
        this.head = new Node('.');  //dummy node 
        this.pos = this.head;     
    }
    
    public void addText(String text) {
        Node temp = this.pos;
        for(char c: text.toCharArray()){
            Node n = new Node(c);
            n.prev = temp;
            n.next = temp.next;
            if (temp.next != null) temp.next.prev = n;
            temp.next = n;
            temp = temp.next;
        }
        this.pos = temp;
        // System.out.println("add");
        return;
    }
    
    public int deleteText(int k) {
        int shift = 0;
        Node temp = this.pos;
        Node temp_next = temp.next;
        while (shift < k && temp != head){
            temp = temp.prev;
            temp.next = null;
            shift++;
        }
        this.pos = temp;
        this.pos.next = temp_next;
        if(temp_next != null){
            temp_next.prev = this.pos;
        }
        // System.out.println("delete");
        return shift;
    }
    
    public String cursorLeft(int k) {
        int shift = 0;
        Node temp = this.pos;
        while (shift < k && temp.prev != null ){
            temp = temp.prev;
            shift++;
        }
        this.pos = temp;
        // System.out.println("left");
        return lastString();
    }
    
    public String cursorRight(int k) {
        int shift = 0;
        Node temp = this.pos;
        while(shift < k && temp.next != null){
            temp = temp.next;
            shift++;
        }
        this.pos = temp;
        // System.out.println("right");
        return lastString();
    }

    private String lastString(){
        Node temp = this.pos;
        StringBuilder st = new StringBuilder();
        int count = 0;
        while( count < 10 && temp != head){
            st.append(temp.val);
            temp = temp.prev;
            count++;
        }

        return st.reverse().toString();

    }
}

class Node{
    char val;
    Node next;
    Node prev;

    public Node(char c){
        this.val = c;
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = new TextEditor();
 * obj.addText(text);
 * int param_2 = obj.deleteText(k);
 * String param_3 = obj.cursorLeft(k);
 * String param_4 = obj.cursorRight(k);
 */