from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dictionary to represent the graph
        graph_edge = {}
        # array to track the number of prerequisites for each course
        inorder = [0] * numCourses
        taken_class = 0

        # Build the graph and inorder array
        for i, pre in enumerate(prerequisites):
            inorder[pre[0]] += 1
            if pre[1] in graph_edge:
                graph_edge[pre[1]].append(pre[0])
            else:
                graph_edge[pre[1]] = [pre[0]]
        # Initialize the queue with courses that have no prerequisites
        queue = deque([])

        # first, add all courses with zero prerequisites to the queue
        for i, n in enumerate(inorder):
            if n == 0:
                queue.append(i)
        
        while queue:
            # take the course at the front of the queue
            cur = queue.popleft()
            taken_class += 1
            # reduce the inorder count for all courses dependent on the current course
            if cur in graph_edge:
                for _, n in enumerate(graph_edge[cur]):
                    if inorder[n] != 0:
                        inorder[n] -= 1
                        if inorder[n] == 0:
                            queue.append(n)

        # check if all courses have been taken
        if taken_class == numCourses:
            return True
        else:
            return False