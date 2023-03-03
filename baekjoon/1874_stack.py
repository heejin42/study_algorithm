import sys
input = sys.stdin.readline


def sol(seq):
    i = 1
    ans = []
    stack = []
    for num in seq:
        while i <= num:
            stack.append(i)
            ans.append('+')
            i += 1

        if stack.pop() != num: return "NO"
        ans.append('-')
    return '\n'.join(ans)


if __name__ == "__main__":
    n = int(input())
    seq = [int(input()) for _ in range(n)]
    print(sol(seq))