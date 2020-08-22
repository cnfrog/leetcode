package leetcode.editor.cn;
//给定一个未排序的整数数组，找出最长连续序列的长度。 
//
// 要求算法的时间复杂度为 O(n)。 
//
// 示例: 
//
// 输入: [100, 4, 200, 1, 3, 2]
//输出: 4
//解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。 
// Related Topics 并查集 数组 
// 👍 503 👎 0


import java.util.HashSet;
import java.util.Set;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution128 {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set_num = new HashSet<>();
        for (int num : nums) {
            set_num.add(num);
        }
        int a = 0;
        for (int num : set_num) {
            if (!set_num.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;
                while (set_num.contains(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }
                a = Math.max(a, currentStreak);
            }
        }
        return a;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
