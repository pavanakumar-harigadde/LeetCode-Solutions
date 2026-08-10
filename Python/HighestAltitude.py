#1732. Find the Highest Altitude

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_altitude=0
        current_altitude = 0
        n=len(gain)
        for g in gain:
            current_altitude += g
            if current_altitude > max_altitude :
                max_altitude = current_altitude

        return max_altitude
