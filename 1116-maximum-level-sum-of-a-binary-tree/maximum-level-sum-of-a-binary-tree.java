/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxLevelSum(TreeNode root) {
        if(root == null) return 0;

        int[] res = new int[] {0,Integer.MIN_VALUE};
        int level = 0;

        Queue<TreeNode> queue = new LinkedList();
        queue.add(root);

        while(queue.size() > 0){
            level++;

            int sum = 0;
            int size = queue.size();

            for(int i=0;i<size;i++){
                TreeNode n = queue.poll();
                sum += n.val;

                if(n.left != null){
                    queue.add(n.left);
                }
                if(n.right != null){
                    queue.add(n.right);
                }
            }

            if(sum > res[1]){
                res[0] = level;
                res[1] = sum;
            }
        }

        return res[0];
    }
}