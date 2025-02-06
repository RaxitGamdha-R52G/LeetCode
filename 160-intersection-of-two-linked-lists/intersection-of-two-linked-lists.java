/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public int len(ListNode head){
        if(head == null) return 0;
        return 1 + len(head.next);
    }

    public ListNode moveHead(ListNode head, int shift){
        for(int i = 0; i< shift; i++){
            head = head.next;
        }
        return head;
    }

    public ListNode compare(ListNode headA, ListNode headB){
        if(headA == null || headB == null) return null;
        if(headA == headB) return headA;
        return compare(headA.next, headB.next);
    }

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int len1 = len(headA);
        int len2 = len(headB);

        if(len1 > len2){
            headA = moveHead(headA, len1-len2);
        }else if(len1 < len2){
            headB = moveHead(headB, len2-len1);
        }

        ListNode result = compare(headA,headB);
        return result;
    }
}