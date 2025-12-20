class MedianFinder:

    def __init__(self):
        # heap for small half and large half
        self.small_heap = [] # maxheap (we use negative values to simulate maxheap in python)
        self.large_heap = [] # minheap


    def addNum(self, num: int) -> None:
        cur_number = len(self.small_heap) + len(self.large_heap) 
        # keep the size property: small_heap can only be equal or 1 element larger than large_heap
        if cur_number % 2 == 0:
            heapq.heappush(self.small_heap,-num)
        else:
            heapq.heappush(self.large_heap,num)
        # only 1 element added, no need to balance    
        if cur_number == 0:
            return
        # balance the two heaps to maintain the order property
        # if reverse order found, swap the roots
        if (-self.small_heap[0]) > self.large_heap[0]:
            swap_small = -heapq.heappop(self.small_heap)
            swap_large = heapq.heappop(self.large_heap)

            heapq.heappush(self.large_heap,swap_small)
            heapq.heappush(self.small_heap,-swap_large)





    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            return (self.large_heap[0] - self.small_heap[0])/2
        else:
            # small_heap is always same or longer than large_heap
            return float(-self.small_heap[0])

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()