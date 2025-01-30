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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> stack1 = new Stack<Integer>();
        ListNode p = l1;
        while (p!=null){
            stack1.push(p.val);
            p = p.next;
        }
        Stack<Integer> stack2 = new Stack<Integer>();
        
        p = l2;
        while (p!=null){
            stack2.push(p.val);
            p = p.next;
        }

        int carry = 0;

        ListNode prev = null;
        while (stack1.size() != 0 || stack2.size() != 0){
            int val = 0;
            if(stack1.size() != 0){
                val += stack1.pop();
            }
            if(stack2.size() != 0){
                val += stack2.pop();
            }

            val += carry;
            carry = val /10;
            val %= 10;

            ListNode n = new ListNode(val);
            n.next = prev;
            prev = n;
        }
        
        if(carry ==1){
            ListNode n = new ListNode(carry);
            n.next = prev;
            prev = n;
        }

        return prev;
    }
}