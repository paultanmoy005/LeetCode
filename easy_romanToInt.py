class Solution:
    Dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    def romanToInt(self, s):
        if len(s)==1:
            return self.Dict[s]
        else:
            if self.Dict[s[0]] < self.Dict[s[1]]:
                sign = -1
            else:
                sign = 1
            return sign * self.Dict[s[0]] + self.romanToInt(s[1:len(s)])