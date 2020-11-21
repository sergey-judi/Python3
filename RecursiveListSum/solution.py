def recursive_sum(items):
    result = 0
    for item in items:
        if type(item) is list:
            result += recursive_sum(item)
        else:
            result += item
    return result


def main():
    test_lists = [
        [1, [1], [1, 1], [1, 1, 1], [1, 1, 1, 1]],
        [[1], [1], [1], [1], [1], [1], [1], [1]],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    for test_list in test_lists:
        print('Sum of list', test_list, 'is:', recursive_sum(test_list))


if __name__ == '__main__':
    main()
