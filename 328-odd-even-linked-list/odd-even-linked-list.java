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
    public ListNode oddEvenList(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode odd = new ListNode(1); // dummy odd node
        ListNode even = new ListNode(0); // dummy even node

        ListNode p = head;
        ListNode t_o = odd;
        ListNode t_e = even;
        int count = 1;
        while (p!=null){
            boolean isOdd = ((count)%2==1);
            ListNode n = new ListNode(p.val);
            if (isOdd){
                t_o.next = n;
                t_o = t_o.next;

            }else{
                t_e.next = n;
                t_e = t_e.next;
            }
            p = p.next;
            count++;
        }
        t_o.next = even.next;
        return odd.next;
        
    }
}