from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [cnt for cnt in count.values()]
        heapq.heapify_max(maxHeap)

        time = 0
        q = deque() # pairs of [cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1 # how many more times this character needs to be placed
                if cnt > 0:
                    q.append([cnt, time + n]) # time + n tells us when this character is available to use again
            
            if q and q[0][1] == time: # q[0][1] is idle time of first queue item (cnt)
                heapq.heappush_max(maxHeap, q.popleft()[0]) # insert cnt back into queue
        
        return time


            

            
