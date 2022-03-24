class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        
        adjList = {i:[] for i in range(numCourses)}
        inDegrees = [0]*numCourses
        
#       Create Adjacency List and inDegrees array
        for p in prerequisites:
            adjList[p[1]].append(p[0])
            inDegrees[p[0]] += 1

        q = deque()

#       Add all courses with no prereqs (in-degrees == 0) to the q
        for i in range(numCourses):
            if inDegrees[i] == 0: q.append(i)
        
#       count keeps track of nodes/courses that we can detach/take
        count = 0
        while q:
            count += 1
            course = q.pop()
            
            for nextCourse in adjList[course]:
                inDegrees[nextCourse] -= 1
                if inDegrees[nextCourse] == 0:
                    q.append(nextCourse)
        
        return True if count == numCourses else False
