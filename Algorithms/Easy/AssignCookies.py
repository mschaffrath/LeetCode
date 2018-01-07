# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
# Each child i has a greed factor gi, which is the minimum size of a
# cookie that the child will be content with; and each cookie j has a size sj.
# If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.

# Note:
# You may assume the greed factor is always positive. 
# You cannot assign more than one cookie to one child.


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        if(not s or not g):
            return 0
        
        import heapq

        heapq.heapify(g)
        heapq.heapify(s)
        
        content = 0
        while not ( len(s) == 0 or len(g) == 0 ):
            if(s[0] >= g[0]):
                content += 1
                heapq.heappop(g)
            heapq.heappop(s)
        return content


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        import Queue as Q

        q_s = Q.PriorityQueue()
        q_g = Q.PriorityQueue()
        
        for p in range(0, len(s)):
            q_s.put(s[p])
        for p in range(0, len(g)):
            q_g.put(g[p])
    
        content = 0
        while not ( q_s.empty() or q_g.empty() ):
            currValS = q_s.get()
            currValG = q_g.get()
            if(currValS >= currValG):
                content += 1
            else:
                q_g.put(currValG)
        return content
        

        
        
        
