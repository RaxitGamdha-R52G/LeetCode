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
    public ListNode rotateRight(ListNode head, int k) {
        int count = 0;
        ListNode p = head;
        while (p != null){
            count++;
            p = p.next;
        }
        if(count == 0){
            return null;
        }
        k = k%count;
        p = head;

        if(k == 0){
            return head;
        }

        for(int i =0; i< k;i++){
            p = p.next;
        }
        ListNode q = head;
        while(p.next != null){
            q = q.next;
            p = p.next;
        }
        ListNode temp = q.next;
        q.next = null;
        
        p = head;
        head = temp;
        while(temp.next != null){
            temp = temp.next;
        }
        temp.next = p;
        return head;

    }
}