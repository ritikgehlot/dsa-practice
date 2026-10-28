from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def calc(starts1, durations1, starts2, durations2):
            earliest_end = min(
                s + d for s, d in zip(starts1, durations1)
            )

            return min(
                max(s, earliest_end) + d
                for s, d in zip(starts2, durations2)
            )

        land_then_water = calc(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )

        water_then_land = calc(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(land_then_water, water_then_land)