def is_prime(number: int) -> bool:
    divisors = [i for i in range(1,number + 1) if number % i == 0]
    return len(divisors) == 2
def main():
    print(is_prime("61"))
if __name__ == '__main__':
    main()