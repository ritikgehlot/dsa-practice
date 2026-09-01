class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()

        answer = 0
        current = 0
        farthest = 0
        i = 0
        n = len(clips)

        while current < time:
            while i < n and clips[i][0] <= current:
                farthest = max(farthest, clips[i][1])
                i += 1

            if farthest == current:
                return -1

            current = farthest
            answer += 1

        return answer