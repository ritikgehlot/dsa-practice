class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        buckets = [0] * k

        def backtrack(index):

            if index == len(nums):
                return True

            num = nums[index]

            for i in range(k):

                if buckets[i] + num > target:
                    continue

                # Avoid equivalent empty buckets
                if i > 0 and buckets[i] == buckets[i - 1]:
                    continue

                buckets[i] += num

                if backtrack(index + 1):
                    return True

                buckets[i] -= num

                # If this number couldn't fit in an empty bucket,
                # don't try other empty buckets.
                if buckets[i] == 0:
                    break

            return False

        return backtrack(0)