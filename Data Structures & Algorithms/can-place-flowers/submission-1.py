class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        if n > len(flowerbed): return False
        
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 else False
        i = 1

        if flowerbed[0] == 0:
            if flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
                i = 2

        while i < len(flowerbed) - 1:
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        
        if flowerbed[-1] == 0:
            if flowerbed[-2] == 0:
                flowerbed[-1] = 1
                n -= 1
        
        return n <= 0


