#!/usr/bin/python3
import numpy as np

def main():
    print("hello")
    res = np.random.rand(100, 100)
    np.savetxt('test.txt', res)


if __name__ == '__main__':
    main()
