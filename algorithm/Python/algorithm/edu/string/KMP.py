# KMP Algorithm 구현

def make_pi(pettern):
    """
    :param pettern: 평문에서 찾을 문자열 
    :return: 건너 뛸 수 있는 문자열의 길이
    """
    n, j = len(pettern), 0
    pi = [0] * n
    for i in range(1, n):
        while j > 0 and pettern[i] != pettern[j]:
            j = pi[j-1]
        if pettern[i] == pettern[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(string, pettern):
    """
    kmp의 핵심은 접두사와 접미사!

    위에서 구한 접두사/접미사를 바탕으로 주어진 문자열의 0~i까지 부분 문자열 중 접두사와 접미사가 같을 수 있는

    부분 문자열 중에서 가장 긴 것의 길이를 담은 pi 배열을 구해야한다.

    이를 이용하여 복잡도를 O(MN)에서 O(M+N)으로 줄일 수 있다.

    i는 입력받은 평문을 순차적으로 탐색하는 index이며 j는 pattern을 탐색하는 index이다. pi 배열에는 해당 인덱스 다음에 평문과 패턴이 일치하지 않는 경우

    되돌아갈 pettern index를 저장한다. 이를 통해 계산횟수를 줄여 O(N+M)의 복잡도를 가질 수 있다.

    :param string: 패턴이 담겨있는지 찾아볼 문자열
    :param pettern: 평문에서 찾아낼 패턴
    :return 패턴이 일치하는 지점의 index들
    """
    pi = make_pi(pettern)
    n, m, j = len(string), len(pi), 0
    ans = []
    for i in range(n):
        while j > 0 and string[i] != pettern[j]:
            j = pi[j-1]
        if string[i] == pettern[j]:
            if j == m - 1:
                ans.append(i - m + 1)
                j = pi[j]
            else:
                j += 1
    return ans

def main():
    string = "ABABABABBABABABABCFCYGABABABABCABABABABC"
    pettern = "ABABABABC"
    print(kmp(string, pettern))


if __name__ == '__main__':
    main()
