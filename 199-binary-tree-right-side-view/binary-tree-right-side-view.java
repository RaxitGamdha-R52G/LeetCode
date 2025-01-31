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
    int max_depth = -1;

    public void rightSide(TreeNode root, int level, List<Integer> res){
        if(root == null){
            return;
        }

        if(max_depth < level){
            res.add(root.val);
            max_depth = level;
        }

        rightSide(root.right, level+1, res);
        rightSide(root.left, level+1, res);
    }

    public List<Integer> rightSideView(TreeNode root) {
        // if(root == null){
        //     return new ArrayList<Integer>();
        // }

        // List<Integer> res = new ArrayList<Integer>();
        // Queue<TreeNode> queue = new LinkedList<TreeNode>();

        // queue.add(root);
        // int size = queue.size();
        // while (size > 0){
        //     TreeNode rightMost = null;
        //     for(int i = 0; i< size; i++){
        //         TreeNode n = queue.remove();
        //         rightMost = n;

        //         if(n.left != null){
        //             queue.add(n.left);
        //         }
        //         if(n.right != null){
        //             queue.add(n.right);
        //         }
        //     }
        //     res.add(rightMost.val);
        //     size = queue.size();
        // }

        // return res;
        List<Integer> res = new ArrayList<Integer>();
        rightSide(root, 0, res);
        return res;
    }
}