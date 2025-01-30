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

    private static int carry[] = new int[] {
        0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1
    };
    private static int num[] = new int[] {
        0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8
    };

    public ListNode doubleIt(ListNode head) {
        // Solution 1
        // if (head == null){
        //     return head;
        // }
        // Stack<ListNode> st = new Stack<ListNode>();

        // ListNode p = head;
        // while (p!=null){
        //     ListNode q = p;
        //     p = p.next;
        //     st.push(q);
        // }

        // ListNode prev = null;
        // int carry = 0;

        // while (st.size() != 0){
        //     ListNode q = st.pop();
        //     int val = q.val;
        //     val <<= 2;
        //     val += carry;
        //     q.val = val % 10;
        //     carry = val / 10;
        //     q.next = prev;
        //     prev = q;
        // }

        // if(carry > 0){
        //     ListNode q = new ListNode(carry);
        //     q.next = prev;
        //     prev = q;
        // }

        // return prev;

        // Solution 2

        if(head == null){
            return head;
        }

        ListNode dummy = new ListNode(0,head);
        ListNode prev = dummy;
        ListNode curr = head;

        while (curr != null){
            int val = curr.val << 1;
            prev.val += carry[val];
            curr.val = num[val];
            prev = curr;
            curr = curr.next;
        }

        return dummy.val ==1 ? dummy: head;
    }
}