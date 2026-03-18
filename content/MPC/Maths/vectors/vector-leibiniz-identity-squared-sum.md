
used in ![[Q-Algebr-and-modulus-of-vectors#problem (unintuitive but inituitive way exists solve for a+b+c maximizatio)]]
# Lagrange's Identity for Squared Distances

i < j implies it is a cyclic sum 

**Identity:**
$$\sum_{1 \leq i < j \leq n} |\vec{v}_i - \vec{v}_j|^2 = n \sum_{i=1}^n |\vec{v}_i|^2 - \left| \sum_{i=1}^n \vec{v}_i \right|^2$$

just expand , key step n-1 is ${}^{n-1}C_{2-1}$
## **Derivation:**


  **Individual Pair Expansion:**
  $|\vec{v}_i - \vec{v}_j|^2 = |\vec{v}_i|^2 + |\vec{v}_j|^2 - 2(\vec{v}_i \cdot \vec{v}_j)$

  **Summing Magnitudes:**
  Since each vector $\vec{v}_k$ appears in exactly $(n-1)$ pairs within the set of $\binom{n}{2}$ combinations:
  $\sum_{i < j} (|\vec{v}_i|^2 + |\vec{v}_j|^2) = (n-1) \sum_{i=1}^n |\vec{v}_i|^2$

  **Summing Dot Products:**
  Utilizing the multinomial expansion of the resultant vector magnitude:
 $|\sum_{i=1}^n \vec{v}_i|^2 = \sum_{i=1}^n |\vec{v}_i|^2 + 2 \sum_{i < j} (\vec{v}_i \cdot \vec{v}_j)$
 $\implies   - 2 \sum_{i < j} (\vec{v}_i \cdot \vec{v}_j) = \sum_{i=1}^n |\vec{v}_i|^2 - |\sum_{i=1}^n \vec{v}_i|^2$

  **Final Synthesis:**
    $\sum_{i < j} |\vec{v}_i - \vec{v}_j|^2 = \underbrace{(n-1) \sum |\vec{v}_i|^2}_{\text{Step 2}} + \underbrace{\sum |\vec{v}_i|^2 - |\sum \vec{v}_i|^2}_{\text{Step 3}}$
    $\sum_{i < j} |\vec{v}_i - \vec{v}_j|^2 = n \sum_{i=1}^n |\vec{v}_i|^2 - |\sum_{i=1}^n \vec{v}_i|^2$

# link with centroid

$\vec{G} = \frac{1}{n} \sum_{i=1}^n \vec{v}_i \implies \sum_{i=1}^n \vec{v}_i = n \vec{G}$
$\sum_{1 \leq i < j \leq n} |\vec{v}_i - \vec{v}_j|^2 = n \sum_{i=1}^n |\vec{v}_i|^2 - |n\vec{G}|^2 = n \left( \sum_{i=1}^n |\vec{v}_i|^2 - n|\vec{G}|^2 \right)$

$\sum_{i=1}^n |\vec{v}_i - \vec{G}|^2 = \sum (|\vec{v}_i|^2 - 2\vec{v}_i \cdot \vec{G} + |\vec{G}|^2) = \sum |\vec{v}_i|^2 - 2(n\vec{G}) \cdot \vec{G} + n|\vec{G}|^2 = \sum |\vec{v}_i|^2 - n|\vec{G}|^2$
$\sum_{1 \leq i < j \leq n} |\vec{v}_i - \vec{v}_j|^2 = n \sum_{i=1}^n |\vec{v}_i - \vec{G}|^2$
