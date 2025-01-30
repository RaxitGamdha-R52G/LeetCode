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
    public ListNode doubleIt(ListNode head) {
        if (head == null){
            return head;
        }
        Stack<ListNode> st = new Stack<ListNode>();

        ListNode p = head;
        while (p!=null){
            ListNode q = p;
            p = p.next;
            st.push(q);
        }

        ListNode prev = null;
        int carry = 0;

        while (st.size() != 0){
            ListNode q = st.pop();
            int val = q.val;
            val *= 2;
            val += carry;
            q.val = val % 10;
            carry = val / 10;
            q.next = prev;
            prev = q;
        }

        if(carry > 0){
            ListNode q = new ListNode(carry);
            q.next = prev;
            prev = q;
        }

        return prev;

    }
}