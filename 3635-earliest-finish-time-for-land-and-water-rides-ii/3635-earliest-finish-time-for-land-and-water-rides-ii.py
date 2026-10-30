
from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def calculate(start1, duration1, start2, duration2):
            earliest_end = min(
                s + d for s, d in zip(start1, duration1)
            )

            return min(
                max(s, earliest_end) + d
                for s, d in zip(start2, duration2)
            )

        land_first = calculate(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )

        water_first = calculate(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(land_first, water_first)
