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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null || head.next == null) return null;
        ListNode p=head, q=head;
        for(int i = 0; i< n; i++){
            p = p.next;
        }
        if(p == null && q== head){
            return head.next;
        }

        while( p != null && p.next != null){
            p = p.next;
            q = q.next;
        }
        q.next= q.next.next;
        return head;
    }
}