Binomial operator
$$
{n \choose k} \\
(x+y)^r = \sum_{i=0}^{r} (x)^{i} (y)^{r-i} \\
$$


$$
n! = n^{n} e^{-n} \sqrt{2 \pi n} (1+O(1/n)) \\
$$

1. Prove  $2^{n+1} = \Theta(2^n)$
$$
0 \leq 2^{n+1} = 2 \cdot 2^{n} \leq c \cdot 2^n, \forall n \geq 0, if c \geq 2 \\
\therefore \text{we can choose } c = 2, n_0 = 1, 0 \leq 2^{n+1} \leq c 2 ^n, \forall n \geq n_0 \\
$$


Prove $(n+a)^b = \Theta(n^b)$
$$
n + a \leq n + |a| \leq 2n, \text{ choose } n_0 = |a| \\
n + a \geq n - |a| \geq \frac{1}{2}n, \text{ choose } n_0 = 2|a| \\
$$

To show that $(n+a)^b = O(n^b)$:
if you choose $n_0 = 2|a|$, then $(2|a|)^b$, then $c = 2^b$
- we let $n_0$ = |a| => $0 \leq (n+a)^b \leq (2n^b) = 2^b n^b$
- What is the takaway?
    - choose an $n_0$, you know that 2n is always greater than n + |a| 
    - cuz as long as n is greater than |a|, you have 2 terms growing on the right, 2n and only one on the left (n), |a| does not grow since its a constant, and this inequality is TRUE when you pick n's above |a| so that makes your $n_0$ 

To show that $(n+a)^b = \Omega(n^b)$
if you choose $n_0 = (1/2)|a|$, then $((1/2)|a|)^b$, then $c = (\frac{1}{2})^b$
- this is the same idea you ask yourself 
- if you pick an $n_0$ where n has to be greater than $2|a|$
- we need to show that $0 \leq c * n^b \leq (n+a)^b$ for some c and for all n greater than $n_0$
- we let $n_0$ = 2 |a| => $0 \leq (1/2)^b n^b = (\frac{1}{2}n)^b \leq (n+a)^b$
- you can choose $n_0$ as 2|a|, 
- what is the takeaway?
    -  
    - 
    - 


To prove $n^n = o(2^n)$
$$
\lim_{n \rightarrow \infty} \frac{2^n}{n^n} \\
\lim_{n \rightarrow \infty} \frac{2^n}{(2n/2)^n} \\
\lim_{n \rightarrow \infty} \frac{2^n}{2^n(n/2)^n} \\
\lim_{n \rightarrow \infty} \frac{1}{(n/2)^n} = 0\\
\therefore n^n = o(2^n)
$$

Move around limit only if its continous


Prove $\sum_{i=0}^{n-1} i a^i = \frac{a - a^n}{(1-a)^2} - \frac{(n-1)a^n}{1-a}$
$$
\sum_{i=0}^{n-1} ia^i = 0 + 1 * a + 2 a^2 \cdots (n-1)a^{n-1}\\
a \sum_{i=0}^{n-1} ia^i = 0 + a^2 + 2 a^3 \cdots (n-1)a^n\\
$$

Strong induction:
$ P(k) \forall n_0 \leq k \leq n$
you need to make sure $k_1\leq n$



String induction example
base step n = 4 can be made using 2+2, n = 5 can be made using 5
induction hypotehsis: assume $\forall k \in [4,n]$, $k can be made using $2 and $5
induction step: (n+1) = (n-1) + 2 and n - 1 can be made using $2 and $5

- do casses for any proof, need to cover all cases, all be disjoint, mutually exclusive


NOTE:
when you are comparing 2 exponential functions with different basis you can take the log of both sides for example $2^n$ and $3^n$.


$$
\lim_{n \rightarrow \infty} \frac{2^n}{3^n} = \lim_{n \rightarrow \infty} log(\frac{2^{n^2}}{3^n}) = n^2 log(2) - n log(3) 
$$
