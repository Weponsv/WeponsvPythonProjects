time_left = int(input())
ready_time = int(input())

if ready_time < 0 or time_left < 0:
    print(-1)
elif time_left >= ready_time:
    print(0)
else:
    stop = False
    count = 0
    while not stop:
        count += 1
        ready_time -= 780

        if time_left >= ready_time:
            stop = True
            print(count)