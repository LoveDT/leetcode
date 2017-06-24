class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num or num < 1:
            return False
        if num < 7:
            return True
        if num % 2 == 0:
            return self.isUgly(num / 2)
        elif num % 3 == 0:
            return self.isUgly(num / 3)
        elif num % 5 == 0:
            return self.isUgly(num / 5)
        else:
            return False
        