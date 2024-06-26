class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = []
        def countProvinces(city):
            visited.append(city)
            all_visited = False
            for i,nCity in enumerate(isConnected[city]):
                if i not in visited and nCity == 1:
                    all_visited = True
                    countProvinces(i)
            return 
        num_provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                countProvinces(i)
                if len(visited) <= len(isConnected):
                    num_provinces+=1

        return num_provinces


# N^2 complexity (not great)