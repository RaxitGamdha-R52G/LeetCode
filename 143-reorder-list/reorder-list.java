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
    public void reorderList(ListNode head) {
        if(head == null){
            return;
        }

        ArrayList<Integer> arr = new ArrayList<Integer>();
        ListNode p = head;

        while(p != null){
            arr.add(p.val);
            p = p.next;
        }

        p = head;

        int i = 0;
        int j = arr.size()-1;

        while (i<=j){
            if(i != j){
                p.val = arr.get(i);
                p = p.next;
            }
            p.val = arr.get(j);
            p = p.next;
            i++;
            j--;
        }
    }
}