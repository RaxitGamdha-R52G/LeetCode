/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    private Node prev = null;

    private void flattenList(Node node){
        if(node == null){
            return;
        }

        flattenList(node.next);
        flattenList(node.child);
        node.next = prev;
        if (prev != null){
            prev.prev = node;
        }
        node.child = null;
        prev = node;
    }

    public Node flatten(Node head) {
        flattenList(head);
        return head;
    }
}