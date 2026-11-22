class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        # First arrange everything in timestamp sequence
        arr = list(zip(timestamp,username,website))
        arr.sort()

        # create a map of username and website
        mp = defaultdict(list)

        for time, name, website in arr:
            mp[name].append(website)
        

        # Now for each user get all the patterns and the count per pattern
        pattern_count = defaultdict(int)
        for user in mp:
            websites = mp[user]
            N = len(websites)
            patterns = set()
            for i in range(N-2):
                for j in range(i+1,N-1):
                    for k in range(j+1,N):
                        patterns.add((websites[i],websites[j],websites[k]))
            
            for p in patterns:
                pattern_count[p] +=1
        
        max_count = 0
        max_pattern = None

        for p in pattern_count:

            if pattern_count[p] > max_count or pattern_count[p] == max_count and p < max_pattern:
                max_count = pattern_count[p]
                max_pattern = p
        
        return list(max_pattern)
        





        