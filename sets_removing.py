def remove_duplicates(some_list):
    set_without_duplicates = set(some_list)
    return list(set_without_duplicates)

def main():
    random_list = [1,1,2,4,2]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    main()