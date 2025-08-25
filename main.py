
# function of calculating fibonacci numbers
def caching_fibonacci(n, memo={}):
    cache = {}
    def fibonacci(n):
        if n <=0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]
    print(cache)
    return fibonacci(n)
