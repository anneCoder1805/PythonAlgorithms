import math
import itertools
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        nums = ["".join(x) for x in list(itertools.permutations(list(str(N))))]
        for n in nums:
            if n[0]!='0':
                a = int(math.log(int(n),2))
                if 2**a == int(n):
                    return True
        return False
