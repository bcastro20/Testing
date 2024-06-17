import matplotlib
import numpy as np
import pandas as pd


# Problem 1: Multiples of 3 and 5

def sum_of_multiples(limit):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)

if __name__ == "__main__":
    print(sum_of_multiples(1000))
# Problem 2: Even Fibonacci numbers

def sum_of_even_fibonacci(limit):
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

if __name__ == "__main__":
    print(sum_of_even_fibonacci(4000000))
# Problem 3: Largest prime factor

def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(data, title, xlabel, ylabel, bins=50):
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Binomial distribution
binomial_data = np.random.binomial(n=10, p=0.5, size=1000)
plot_histogram(binomial_data, 'Binomial Distribution (n=10, p=0.5)', 'Value', 'Frequency')

# Poisson distribution
poisson_data = np.random.poisson(lam=3.0, size=1000)
plot_histogram(poisson_data, 'Poisson Distribution (lambda=3.0)', 'Value', 'Frequency')

# Normal distribution
normal_data = np.random.normal(loc=0, scale=1, size=1000)
plot_histogram(normal_data, 'Normal Distribution (mean=0, std=1)', 'Value', 'Frequency')
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(data, title, xlabel, ylabel, bins=50, density=False, color='blue', alpha=0.5):
    plt.hist(data, bins=bins, edgecolor='black', alpha=alpha, density=density, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

# Parameters for the distributions
n_values = [10, 50, 100, 500, 1000]
p = 0.5

# Plot histogram
for n in n_values:
    plt.figure(figsize=(12, 6))
    
    # Binomial distribution
    binomial_data = np.random.binomial(n=n, p=p, size=10000)
    plot_histogram(binomial_data, f'Binomial Distribution (n={n}, p={p})', 'Value', 'Frequency', density=True, color='blue', alpha=0.5)
    
    # Normal distribution
    mean = n * p
    stddev = np.sqrt(n * p * (1 - p))
    normal_data = np.random.normal(loc=mean, scale=stddev, size=10000)
    plot_histogram(normal_data, f'Normal Distribution (mean={mean}, stddev={stddev})', 'Value', 'Frequency', density=True, color='red', alpha=0.5)
    
    plt.legend(['Binomial', 'Normal'])
    plt.show()
# Demonstrating Convergence of Binomial to Normal Distribution


## Method
We generated Binomial distributions with increasing values of \( n \) and compared them to the corresponding Normal distributions with the same mean and standard deviation.

## Results

### \( n = 10 \)
![Binomial vs Normal (n=10)](images/binomial_vs_normal_n10.png)

### \( n = 50 \)
![Binomial vs Normal (n=50)](images/binomial_vs_normal_n50.png)

### \( n = 100 \)
![Binomial vs Normal (n=100)](images/binomial_vs_normal_n100.png)

### \( n = 500 \)
![Binomial vs Normal (n=500)](images/binomial_vs_normal_n500.png)

### \( n = 1000 \)
![Binomial vs Normal (n=1000)](images/binomial_vs_normal_n1000.png)

## Conclusion
The histograms clearly show that as \( n \) increases, the Binomial distribution becomes more similar to the Normal distribution, thus visually demonstrating the Central Limit Theorem in action.

