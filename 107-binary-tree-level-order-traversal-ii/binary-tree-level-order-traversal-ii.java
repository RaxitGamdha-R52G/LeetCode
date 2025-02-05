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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        if(root == null){
            return new ArrayList<>();
        }
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> tempAns;
        Queue<TreeNode> temp = new LinkedList<>();

        temp.add(root);

        while(temp.size() > 0){
            tempAns = new ArrayList<Integer>();
            int size = temp.size();
            for(int i = 0; i< size;i++){
                TreeNode n = temp.remove();
                tempAns.add(n.val);

                if(n.left != null){
                    temp.add(n.left);
                }
                if(n.right != null){
                    temp.add(n.right);
                }
            }
            ans.add(tempAns);
        }

        Collections.reverse(ans);

        return ans;
    }
}