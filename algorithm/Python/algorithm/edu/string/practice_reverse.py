def my_reverse(string):
    arr = list(string)
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

    return "".join(arr)


def main():
    test = "1234"
    try:
        assert my_reverse(test) == test[::-1]
        print(my_reverse(test))
    except AssertionError:
        print("error")


if __name__ == '__main__':
    main()
