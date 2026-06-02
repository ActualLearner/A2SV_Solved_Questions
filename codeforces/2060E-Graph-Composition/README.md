# 2060E-Graph-Composition

**Problem:** [2060E-Graph-Composition](https://codeforces.com/problemset/problem/2060/E)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

You are given two simple undirected graphs F and G with n vertices. F has m_1 edges while G has m_2 edges. You may perform one of the following two types of operations any number of times:

 
-  Select two integers u and v (1 ≤q u,v ≤q n) such that there is an edge between u and v in F. Then, remove that edge from F. 
-  Select two integers u and v (1 ≤q u,v ≤q n) such that there is no edge between u and v in F. Then, add an edge between u and v in F. 
Determine the minimum number of operations required such that for all integers u and v (1 ≤q u,v ≤q n), there is a path from u to v in F if and only if there is a path from u to v in G.


**Input**

The first line contains an integer t (1 ≤q t ≤q 10⁴) — the number of independent test cases.

The first line of each test case contains three integers n, m_1, and m_2 (1 ≤q n ≤q 2⋅ 10⁵, 0 ≤q m_1,m_2 ≤q 2⋅ 10⁵) — the number of vertices, the number of edges in F, and the number of edges in G.

The following m_1 lines each contain two integers u and v (1 ≤q u, v≤q n) — there is an edge between u and v in F. It is guaranteed that there are no repeated edges or self loops.

The following m_2 lines each contain two integers u and v (1 ≤q u,v≤q n) — there is an edge between u and v in G. It is guaranteed that there are no repeated edges or self loops.

It is guaranteed that the sum of n, the sum of m_1, and the sum of m_2 over all test cases do not exceed 2 ⋅ 10⁵.


**Output**

For each test case, output a single integer denoting the minimum operations required on a new line.


**Example**

**Input**

```
5
3 2 1
1 2
2 3
1 3
2 1 1
1 2
1 2
3 2 0
3 2
1 2
1 0 0
3 3 1
1 2
1 3
2 3
1 2
```

**Output**

```
3
0
2
0
2
```


**Note**

In the first test case you can perform the following three operations: 

 
-  Add an edge between vertex 1 and vertex 3. 
-  Remove the edge between vertex 1 and vertex 2. 
-  Remove the edge between vertex 2 and vertex 3.  It can be shown that fewer operations cannot be achieved.In the second test case, F and G already fulfill the condition in the beginning.

In the fifth test case, the edges from 1 to 3 and from 2 to 3 must both be removed.
