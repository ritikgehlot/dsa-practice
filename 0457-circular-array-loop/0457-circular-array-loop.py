class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def nxt(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = fast = i

            while True:
                if nums[slow] == 0 or (nums[slow] > 0) != direction:
                    break

                s = nxt(slow)
                if s == slow:
                    break
                slow = s

                for _ in range(2):
                    if nums[fast] == 0 or (nums[fast] > 0) != direction:
                        fast = -1
                        break
                    f = nxt(fast)
                    if f == fast:
                        fast = -1
                        break
                    fast = f

                if fast == -1:
                    break

                if slow == fast:
                    return True

            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                k = nxt(j)
                nums[j] = 0
                j = k

        return False