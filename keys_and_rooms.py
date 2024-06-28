class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        def fbiOpenUp(door):
            if door in visited:
                return
            else:
                keys = rooms[door]
                visited.add(door)
                for key in keys:
                    fbiOpenUp(key)
                    
        fbiOpenUp(0)
        if len(visited) == len(rooms):
            return True
        else:
            return False
