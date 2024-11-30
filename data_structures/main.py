"""
Max and min heap
* Useful for ordering elements like in priority queue
"""
import heapq


new_heap = []
heapq.heappush(new_heap, 2)
heapq.heappush(new_heap, 3)
heapq.heappush(new_heap, 7)
heapq.heappush(new_heap, 9)

print(new_heap)