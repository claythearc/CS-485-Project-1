import time
import timeit

def exhaustive(b: int,z: int,n: int):
    """Brute Forces the answer to a discrete logarithm problem. """
    x = 0  # type: int
    while True: # loop x increasingly
        if (b**x % n) == z: # if b^x is congruent to z mod n
            print(f"Answer: {x}")  # print the answer
            return x  # return the value
        x = x + 1  # increment x


if __name__ == "__main__":  # run the code here.
    b = int(input("Enter b: "))  # type: int
    z = int(input("Enter z: "))  # type: int
    n = int(input("Enter n: "))  # type: int

    tic = time.process_time()
    # measures execution time, over 1 run
    print(timeit.timeit(f"exhaustive({b},{z},{n})", setup="from __main__ import exhaustive", number=1))
    toc = time.process_time()
    print(f"Process time: {toc-tic}")