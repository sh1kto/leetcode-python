# 🔍 Problem: Two Sum
# 💻 Link: https://leetcode.com/problems/two-sum/
# 🧠 Difficulty: Easy
# 📚 Tags: Array, HashMap

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        💡 Explanation:
        Given an array of integers, return the indices of the two numbers that add up to a specific target.
        We use a hash map to store numbers we've seen and their indices.
        For each number, we check if its complement (target - num) is already in the hash map.
        
        ⏱️ Time Complexity: O(n)
        🛢️ Space Complexity: O(n)
        """
        hashmap = {}  # Dictionary to store the complement of each number
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]  # If complement exists, return indices
            hashmap[num] = i  # Store the number and its index

# 🔧 Example usage
if __name__ == "__main__":
    sol = Solution()
    # Test case 1: Expected [0, 1] because nums[0] + nums[1] == 9
    print(sol.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
