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
    public boolean isPalindrome(ListNode head) {
        StringBuilder st = new StringBuilder();
        ListNode curr = head;

        while(curr != null){
            st.append(curr.val);
            curr = curr.next;
        }
        String s = st.toString();
        st.reverse();
        return s.equals(st.toString());
    }
}