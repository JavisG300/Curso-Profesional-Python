#This closure returns a function that returns the division of an x number by n

from __future__ import division


def make_division_by(n):
    def division(x):
        return x / n
    return division

def main():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_3 = make_division_by(5)
    print(division_by_3(100))

    division_by_3 = make_division_by(18)
    print(division_by_3(54))

if __name__ == "__main__":
    main()


