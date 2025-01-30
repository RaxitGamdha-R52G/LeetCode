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
        // Solution 1
        // ListNode odd = new ListNode(1); // dummy odd node
        // ListNode even = new ListNode(0); // dummy even node

        // ListNode p = head;
        // ListNode t_o = odd;
        // ListNode t_e = even;
        // int count = 1;
        // while (p!=null){
        //     boolean isOdd = ((count)%2==1);
        //     ListNode n = new ListNode(p.val);
        //     if (isOdd){
        //         t_o.next = n;
        //         t_o = t_o.next;

        //     }else{
        //         t_e.next = n;
        //         t_e = t_e.next;
        //     }
        //     p = p.next;
        //     count++;
        // }
        // t_o.next = even.next;
        // return odd.next;

        // Solution 2

        ListNode p1 = head;
        ListNode p2 = head.next;
        ListNode odd = p1;
        ListNode even = p2;

        while( p1 != null && p2 != null && p2.next!= null){
            p1.next = p2.next;
            p2.next = p2.next.next;
            p1 = p1.next;
            p2 = p2.next;
        }

        p1.next = even;

        return odd;
    }
}