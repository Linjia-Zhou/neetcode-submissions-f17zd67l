class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                
                res[i1+i2] += digit
                res[i1+i2+1] += (res[i1+i2] // 10) # if digit is double digits, then we need to add tens-place number to next index. if digit is only single digit, this will return 0 so it would still work
                res[i1+i2] = res[i1+i2] % 10 # if digit is double digits, then it would've made res[i1+i2] double digits as well, so need to mod 10 to only keep ones-place number. if digit is only single digit, this will return digit, so it would still work

        res, zero = res[::-1], 0

        while zero < len(res) and res[zero] == 0: # finding all leading zeroes
            zero += 1

        res = map(str, res[zero:])
        return "".join(res)
