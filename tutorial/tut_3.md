T(n/2) + T(n/3) + n , T(1) = 1
Shortest path is when you divide by larger number
lg_3(n)
lg_2(n)

n = \Theta(lgn)

Total cost = h(tree) * cost per level

Each level you have this amount of work:
$$
T(n) \leq \sum_{i=0}^{lgn - 1} n (5/6)^i
$$

This is a geometric series, converges since its less than 1



To prove equality its often quite difficult, you may want to prove <= and =>:
3=>4
|E| \geq |V| - 1

base: given G satisfies 3 with |V| = 1 and |E| = 0
ind hyp: given G sat 3 w/ |V| = n, then |E| \geq n -1
ind step: let G satsfies 3 w/ |V| = n - 1
V_1 \in V, G' = G - {v_1}
|V'| = n
|E'| \geq n |V'| - 1 = n - 1
|E| \geq |E'| + 1 = |V'| = n =  |V| - 1

other direction 
|E| \leq |V| - 1
assume the instantiation of the graph satisfies 3:
base |V| = 1, |E| = 0, |V| = 2, |E| = 1
ind hyp: if |V| = k then |E| \leq k - 1 \forall k \leq n
step: given G w/ |V| = n + 1, consider some edge e
remove e , get G_1, G_2 connected components
|E| = |E_1| + |E_2| + 1 \leq |V_1| - 1 + |V_2| - 1 + 1

you have to cover all decrements hence 2 base cases

4=> 5
G connected & |E| = |V| - 1, G acyclic & |E| = |V| - 1
Proof by Contradiction:
ATAC that G has some cycle V_1,V_2,...V_k
without loss of generality (covers all cases), cycle is simple, (if it has a cycle it has a simple cycle)
let G_k subgraph containing that cycle, 

to get G_k we remove all vertices that |V| = k vertices , because its connected each vertex has at least 1 adjacent edge
G -> G_k removed |V| - k vertices, \geq |v| - k
|V_k| = |V| - (|V| -k)= k
|E_k| \leq |E| - (|V| -k)
\leq k - 1


$$
|V_k| = K, |E_k| = k
$$


you should write given G satisfies 3 since you cant assume you always have the same graph with same number of nodes


for induction:
\forall conditions that are unspecified we want to prove this proposition
given an instance of the problem, where X equals n + 1