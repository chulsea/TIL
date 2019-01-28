def strcmp(str1, str2):
    n = len(str1)
    if n != len(str2):
        return False
    else:
        for i in range(n):
            if str1[i] != str2[i]:
                return False
    return True

def main():
    str1 = "hello"
    str2 = "hello "
    print(strcmp(str1, str2))

if __name__ == '__main__':
    main()