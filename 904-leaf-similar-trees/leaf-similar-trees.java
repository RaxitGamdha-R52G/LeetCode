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
    public void traverse(TreeNode root, ArrayList<Integer> res){
        if(root == null){
            return;
        }
        if(root.left == null && root.right == null){
            res.add(root.val);
        }
        traverse(root.left, res);
        traverse(root.right, res);
        return;
    }

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> rl1 = new ArrayList<Integer>();
        ArrayList<Integer> rl2 = new ArrayList<Integer>();

        traverse(root1, rl1);
        traverse(root2, rl2);

        return rl1.equals(rl2);
    }
}