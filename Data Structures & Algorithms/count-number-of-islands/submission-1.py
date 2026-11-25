"""
Mark it visited when putting in not taking out! -> no duplicated in the queue
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def bfs(row,col):

            que = deque([(row,col)])
            # mark the position visited
            visited.add((row,col)) 

            while que:
                r,c = que.popleft()

                # add all its children (directions) to queue who have not yet been visited
                for dr,dc in directions:

                    new_r,new_c = r+dr, c+dc

                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == "1" and (new_r,new_c) not in visited:
                        que.append((new_r,new_c))
                        visited.add((new_r,new_c))
        
        # if we see 1 then there is an island. We just need to see how far it extends to
        for r in range(rows):
            for c in range(cols):
                
                # A new island we have not visited:
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands +=1
                    
                    # visit the entire island:
                    bfs(r,c)
        
        return islands

        

                

