/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if(head == null) return null;

        PriorityQueue<Integer> queue = new PriorityQueue<>();
        ListNode temp = head;
        while(temp != null){
            queue.add(temp.val);
            temp = temp.next;
        }

        temp = head;
        while(temp != null){
            temp.val = queue.poll();
            temp = temp.next;
        }

        return head;
    }
}