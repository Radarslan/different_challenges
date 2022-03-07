def get_runner_up_score(n, arr):
    if n in range(2, 11):
        arr = sorted(arr, reverse=True)
        for i in range(1, len(arr)):
            if arr[i] in range(-100, 101) and arr[i] != arr[0]:
                return arr[i]
        return arr[0]


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(get_runner_up_score(n, arr))
