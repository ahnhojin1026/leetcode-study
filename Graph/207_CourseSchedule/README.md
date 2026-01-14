# [LeetCode] 207. Course Schedule

## 📌 Topic
* Graph Theory
* Topological Sort (Kahn's Algorithm)
* Cycle Detection

## 💡 Idea / Intuition
The problem asks if it is possible to finish all courses given dependency constraints (prerequisites).
This is a classic **Dependency Resolution** problem, which can be modeled as finding a topological ordering in a **Directed Graph**.

* **Nodes:** Courses
* **Edges:** Prerequisites ($B \to A$: To take A, you must complete B first).

If the graph contains a **Cycle** (e.g., $A \to B \to A$), it's a deadlock, and you cannot finish all courses.
We use **Kahn's Algorithm**, which repeatedly removes nodes with **0 Indegree** (no unfulfilled prerequisites).

## 📝 Approach
1.  **Initialization:**
    * `graph_edge`: Adjacency list to store the graph ($Source \to [Destinations]$).
    * `inorder`: Array to store the **Indegree** (number of prerequisites) for each course.
2.  **Build Graph:**
    * Iterate through `prerequisites`.
    * Increment `inorder` for the destination course.
    * Add the edge to `graph_edge`.
3.  **Queueing (Bootstrap):**
    * Add all courses with `inorder == 0` (no prerequisites) to the queue. These are the courses we can start immediately.
4.  **Process (BFS):**
    * While the queue is not empty:
        * Pop a course (`cur`) and increment `taken_class` count.
        * Find all courses (`n`) that depend on `cur`.
        * Decrement their `inorder` count (since `cur` is now finished).
        * **Crucial Step:** If `inorder[n]` becomes 0, it means all prerequisites for `n` are met. Add `n` to the queue.
5.  **Result:**
    * If `taken_class` equals `numCourses`, it means we successfully processed all courses (DAG). Otherwise, a cycle exists.

## ⏱️ Complexity
* **Time Complexity:** $O(V + E)$
    * $V$: Number of courses (nodes).
    * $E$: Number of prerequisites (edges).
    * We process each node and edge exactly once.
* **Space Complexity:** $O(V + E)$
    * To store the adjacency list and indegree array.