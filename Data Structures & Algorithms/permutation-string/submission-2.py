class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)+1):
            sorted_s1 = ''.join(sorted(s1))
            sorted_s2_window = ''.join(sorted(s2[i:i+len(s1)]))

            if sorted_s1 == sorted_s2_window:
                return True

        return False