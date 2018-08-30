import time
import timeit

def exhaustive(b: int,z: int,n: int):
    print(f"Called with {b},{z},{n} ")
    """Brute Forces the answer to a discrete logarithm problem. """
    x = 0  # type: int
    while True: # loop x increasingly
        if pow(b, x, n) == z: # if b^x is congruent to z mod n
            print(f"Answer: {x}")  # print the answer
            return x  # return the value
        x = x + 1  # increment x


if __name__ == "__main__":  # run the code here.
    numberlist = [
        [97, 143, 97],
        [2, 19, 3],
        [3, 1452, 1999]
    ]  # type: list(list(int))
    for numset in numberlist:
        tic = time.process_time()
        walltic = time.time()
        # measures execution time, over 1 run
        exhaustive(*numset)
        toc = time.process_time()
        walltoc = time.time()
        print(f"Process time: {toc-tic}")
        print(f"Actual Time: {walltoc - walltic}")