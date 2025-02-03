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
    public ListNode middleNode(ListNode head) {
        if(head == null){
            return null;
        }
        if(head.next == null){
            return head;
        }

        ListNode prev = new ListNode(0), curr = head;
        prev.next= head;

        while(curr != null && curr.next != null){
            prev = prev.next;
            curr = curr.next.next;
        }
        return prev.next;
    }
}