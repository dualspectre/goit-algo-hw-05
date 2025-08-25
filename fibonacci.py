
# function of calculating fibonacci numbers
def caching_fibonacci():
    cache = {}
    # global ref_cache #
    # ref_cache = cache
    def fibonacci(n):
        """
        
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]
    return fibonacci

"""
Testing fibonacci function
"""
# fib = caching_fibonacci()

# print(fib(10))  # Output: 55
# print(fib(5))  # Output: 5
# print(fib(50))  # Output: 12586269025
# print(fib(1000))  # Output: 354224848179261915075
# print(fib(1500))  # Output: 139423224561697880139045790367
# print(fib(2000))  # Output: 280571172992510140037611932413038677189525