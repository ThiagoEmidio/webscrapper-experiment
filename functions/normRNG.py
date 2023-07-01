import random

def normRNG(mean, std_dev_percentage=35, num_std_devs = 2):
    std_dev = mean*(std_dev_percentage/100)
    lower_limit = mean - (num_std_devs * std_dev)
    upper_limit = mean + (num_std_devs * std_dev)
    while True:
        number = random.normalvariate(mean, std_dev)
        if lower_limit <= number <= upper_limit:
            return abs(number)

# i=10
# while i>=1:
#     print([rng(100)])
#     i=i-1
# Wilmington new hampshire
