text = str(input())
from_n = int(input())
to_n = int(input()) + 1

for _ in range(from_n, to_n):
    print(f'{_}-й {text}.')