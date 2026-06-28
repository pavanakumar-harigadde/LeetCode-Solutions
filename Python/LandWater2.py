#3635. Earliest Finish Time for Land and Water Rides II

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        def solve(start1,duration1,start2,duration2):
            finish1=float('inf')
            for s, d in zip(start1,duration1):
                if s + d < finish1:
                    finish1 = s+d

            finish2=float('inf')
            for s,d in zip(start2,duration2):
                current_total_finish = max(s,finish1)+d
                if current_total_finish <finish2:
                    finish2=current_total_finish

            return finish2

        land_then_water = solve(landStartTime, landDuration, waterStartTime, waterDuration)

        water_then_land = solve(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_then_water,water_then_land)
