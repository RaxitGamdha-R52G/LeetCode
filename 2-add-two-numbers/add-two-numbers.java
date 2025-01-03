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
        ListNode end= new ListNode(0,null);
        ListNode temp1=l1,temp2=l2,head = end;
        int carry=0;
        while(temp1!=null || temp2!=null)
        {
            int val=0;
            if(temp1 != null){ 
                val += temp1.val;
                temp1 = temp1.next;
            }
            if(temp2 != null) {
                val += temp2.val;
                temp2 = temp2.next;
            }
            int temp = val + carry;
            val = temp % 10;
            carry = temp / 10;         
            ListNode l=new ListNode(val,null);
            end.next=l;
            end=l;
            
        }
        if(carry==1)
        {
            ListNode l=new ListNode(1,null);
            end.next=l;
            end=l;
        }
        return head.next;
    }
}