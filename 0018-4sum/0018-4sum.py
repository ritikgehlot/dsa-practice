from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n - 3):
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Minimum possible sum for this i
            min_sum = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min_sum > target:
                break

            # Maximum possible sum for this i
            max_sum = nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3]
            if max_sum < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate second numbers
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    current_sum = (
                        nums[i] +
                        nums[j] +
                        nums[left] +
                        nums[right]
                    )

                    if current_sum == target:
                        answer.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        left += 1
                        right -= 1

                        # Skip duplicate left values
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate right values
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif current_sum < target:
                        left += 1

                    else:
                        right -= 1

        return answer