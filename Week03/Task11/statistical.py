import numpy as np

# mean : 
# The mean is the average of the numbers. It is easy to calculate: add up all the numbers,
#  then divide by how many numbers there are.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("mean = ", np.mean(arr)) # 5.5

# median :
# The median is the middle number in a group of numbers. To find the median,
#  put the numbers in order. If there is an odd number of numbers, the middle one is the median.
#  If there is an even number of numbers, average the two middle ones.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("median = ", np.median(arr)) # 5.5

# mode :
# The mode is the number that occurs most often in a set of numbers.
#  To find the mode, list each number that appears in the set of numbers and count how many times it appears.
#  The mode is the number that appears the most times.

""" 
For example, in a dataset containing information about customer purchases, 
mean could be used to calculate the average amount spent by customers, 
while mode could be used to identify the most commonly purchased item. 
These measures are then used to build machine learning models that can 
predict customer behavior or make recommendations.
Overall, mean and mode are important tools in machine learning for 
understanding and analyzing data, as well as building accurate and reliable models.
"""

# standard deviation :
# The standard deviation is a number that describes how spread out the values are from the mean.
#  A low standard deviation means that most of the numbers are close to the mean (average) value.
#  A high standard deviation means that the values are spread out over a wider range.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("standard deviation = ", np.std(arr)) # 2.8722813232690143

# variance :
# The variance is another number that indicates how spread out the values are.
#  In fact, if you take the square root of the variance, you get the standard deviation!
#  So the standard deviation is the square root of the variance.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("variance = ", np.var(arr)) # 8.25

# Quantiles :
# Quantiles are used in statistics to give you a number that describes the value that a given
#  percent of the values are lower than. For example, the median is the 50th percentile.
#  The 25th percentile is also known as the first quartile. The 75th percentile is also known as the third quartile.    
#  The interquartile range is the difference between the third quartile and the first quartile.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("quantiles = ", np.quantile(arr, 0.25)) # 2.75

# Percentiles :
# Percentiles are used in statistics to give you a number that describes the value that a given
#  percent of the values are lower than. For example, the median is the 50th percentile.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("percentiles = ", np.percentile(arr, 50)) # 5.5


# Range :
# The range is the difference between the lowest value and the highest value in a set of data.
#  The range is a simple way to describe the variation in a set of data.
# The range is the most basic measure of variation.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("range = ", np.ptp(arr)) # 9

# ---Probability Distribution---

# Uniform Distribution :
# A uniform distribution is a probability distribution where all outcomes are equally likely.
#  A uniform distribution is also called a rectangular distribution or a rectangular probability distribution.

# Generate random numbers from a uniform distribution over 1 to 50: with equal probability
x = np.random.uniform(low=1, high=50, size=10)
print(x) 
#[31.38440121 34.96622316 46.03156531 48.88605461 18.32913183 28.78652187
# 24.81401737  5.64350323  2.30205173 36.19403233]


# Normal Distribution :
# A normal distribution is a probability distribution that is symmetric around the mean, showing that data near the mean are more frequent in occurrence than data far from the mean.

# Generate random numbers from a normal distribution with mean 0 and standard deviation 1
x = np.random.normal(loc=0, scale=1, size=10)
print(x)


# Binomial Distribution :
# A binomial distribution is a discrete probability distribution of the number of successes in a sequence of n independent experiments, each asking a yes–no question, and each with its own Boolean-valued outcome: success/yes/true/one (with probability p) or failure/no/false/zero (with probability q = 1 − p).

# Generate random numbers from a binomial distribution with 10 trials and probability of success 0.5
x = np.random.binomial(n=10, p=0.5, size=10)
print(x)

# Poisson Distribution :
# A Poisson distribution is a discrete probability distribution that 
# expresses the probability of a given number of events occurring in a 
# fixed interval of time and/or space if these events occur with a known 
# constant rate and independently of the time since the last event.

# Generate random numbers from a Poisson distribution with mean 3
x = np.random.poisson(lam=3, size=10)
print(x)


# Exponential Distribution :
# An exponential distribution is a probability distribution 
# that describes the time between events in a Poisson point process, 
# i.e. a process in which events occur continuously and independently at a constant average rate.

# Generate random numbers from an exponential distribution with mean 1 wit lambda = 0.5
x = np.random.exponential(scale=1/0.5, size=10)
print(x)