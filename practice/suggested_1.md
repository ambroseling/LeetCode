3-4:
a.
If $f(n) = O(g(n))$, it means that $0 \leq f(n) \leq c g(n)$ is true,
This goes against $g(n) = O(f(n))$, means that $0 \leq g(n) \leq c f(n)$


b. 
$$
f(n) + g(n) = \Theta(min(f(x),g(x))) \\
f(n) + g(n) = 0 \lt c_1 min(f(x),g(x)) \lt f(n) + g(n) \lt c_2 min(f(x),g(x))
$$

Assume that $g(n) < f(n)$, or $g(n) = o(f(n))$:
Then:
$$
f(n) + g(n) = 0 \lt c_1 g(n) \lt f(n) + g(n) \lt c_2 g(n)
f(n) + g(n) = 0 \lt c_1  \lt \frac{f(n)}{g(n)} + 1 \lt c_2 
$$
Since the limit of $\lim_{n\rightarrow \infty} \frac{f(n)}{g(n)} = \infty$ goes to infinity, it is not bounded between $c_2$ and $c_1$, hence the proposition must be false


c.
If $f(n) = O(g(n))$, then $lg(f(n)) = O(lg(g(n)))$
Assume it is true, then it is true that 
$$
0 \leq f(n) \leq c g(n) \\ 
0 + d \leq f(n) + d \leq c g(n) + d\\ 
lg(d) \leq 
$$
THis equality holds for sufficiently large n.


$$
T(n) = 2(\lfloor n/2 \rfloor) + n\\

$$

You can fidn the height of the recursion tree like follows:
$$
(1/2)^{k} n =1 \\ 
k * (log(1/2))  = log(1/n) \\
k  = \frac{log(1/n)}{log(1/2)} \\
k = \frac{-log(n)}{-log(2)} \\ 
k = log_2(n) \\
$$

The heigh of the recursion tree is $log(n)$
The cost at each level is $$