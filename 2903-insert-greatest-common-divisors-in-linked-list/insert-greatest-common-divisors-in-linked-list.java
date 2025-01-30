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
    public int gcd(int a, int b){
        while (b!=0){
            int temp = a % b;
            a = b;
            b = temp;
        }

        return a;
    }

    public ListNode insertGreatestCommonDivisors(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }

        ListNode p = head;
        ListNode q = head.next;
        while(p!=null && q!=null){
            int val = gcd(p.val, q.val);
            ListNode n = new ListNode(val);
            n.next = q;
            p.next = n;
            p = q;
            q = q.next;
        }

        return head;
        
    }
}