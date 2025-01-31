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
    public int pairSum(ListNode head) {
        if(head == null){
            return 0;
        }
        int total = 0;
        ListNode curr = head;
        while (curr != null){
            total++;
            curr = curr.next;
        }

        int arr[] = new int[total/2];
        curr = head;

        for(int i = 0;i<arr.length;i++){
            arr[i] = curr.val;
            curr = curr.next;
        }
        for(int i = arr.length -1; i>-1;i--){
            arr[i] += curr.val;
            curr = curr.next;
        }
        int max = arr[0];

        for(int i = 1; i< arr.length; i++){
            max = Math.max(max,arr[i]);
        }

        return max;
    }
}