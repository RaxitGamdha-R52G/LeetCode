class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> s1 = new HashSet<Integer>();
        Set<Integer> s2 = new HashSet<Integer>();
        for(int num:nums1) s1.add(num);
        for(int num:nums2) s2.add(num);

        List<Integer> diff1 = new ArrayList<Integer>();

        for(int num:s1){
            if(!s2.contains(num)){
                diff1.add(num);
            }
        }

        List<Integer> diff2 = new ArrayList<Integer>();

        for(int num:s2){
            if(!s1.contains(num)){
                diff2.add(num);
            }
        }

        return Arrays.asList(diff1,diff2);
    }
}