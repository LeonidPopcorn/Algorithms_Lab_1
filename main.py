import time
import matplotlib.pyplot as plt

def Binary_Search(arr, target, left, right):
    if right <= left:
        return 0
    middle = int((left + right) / 2)
    if arr[middle] == target:
        return 1
    elif arr[middle] < target:
        return Binary_Search(arr, target, middle + 1, right)
    elif arr[middle] > target:
        return Binary_Search(arr, target, left, middle - 1)

def first_alg(matrix, target, N, M, times):
    start_time = time.perf_counter()
    i = 0
    j = N - 1
    while(1):
        if i > M - 1 or j < 0:
            times.append(time.perf_counter() - start_time)
            break
        if matrix[i][j] == target:
            times.append(time.perf_counter() - start_time)
            break
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1

def second_alg(matrix, target, N, M, times):
    start_time = time.perf_counter()
    i = 0
    flag = 0
    while i < M:
        flag = Binary_Search(matrix[i], target, 0, N - 1)
        if flag == 1:
            times.append(time.perf_counter() - start_time)
            break
        elif flag == 0:
            i += 1
    if flag == 0:
        times.append(time.perf_counter() - start_time)

def third_alg(matrix, target, N, M, times):
    start_time = time.perf_counter()
    bound = 1
    i = 0
    while i < M:
        while (bound < N) and (matrix[i][bound] < target):
            bound *= 2
        flag = Binary_Search(matrix[i], target, min(bound, N), bound // 2)
        if flag == 1:
            times.append(time.perf_counter() - start_time)
            break
        elif flag == 0:
            i += 1
    if flag == 0:
        times.append(time.perf_counter() - start_time)

times_first_alg = []
times_second_alg = []
times_third_alg = []
all_avg_times_first_alg = []
all_avg_times_second_alg = []
all_avg_times_third_alg = []
n = []
print("Select with witch data generation do you want to check algorithms work:\n",
      "1) arr[i][j] = (N//M*i+j)*2;  target = 2*N+1\n",
      "2) arr[i][j] = N//M*i*j*2;  target = 16*N+1")
generation = int(input("Mode 1 or 2:"))
for i in range(1, 14):
    n.append(2 ** i)
    if generation == 1:
        M = 2 ** i
        N = 2 ** 13
        matrix = [[int((N // M * i + j) * 2) for j in range(N)] for i in range(M)]
        target = 2 * N + 1
    elif generation == 2:
        M = 2 ** i
        N = 2 ** 13
        matrix = [[int(N // M * i * j * 2) for j in range(N)] for i in range(M)]
        target = 16 * N + 1
    print("With M =", 2 ** i)
    for _ in range(100):
        first_alg(matrix, target, N, M, times_first_alg)
        second_alg(matrix, target, N, M, times_second_alg)
        third_alg(matrix, target, N, M, times_third_alg)
    avg_time_first_alg = sum(times_first_alg)/len(times_first_alg)
    avg_time_second_alg = sum(times_second_alg)/len(times_second_alg)
    avg_time_third_alg = sum(times_third_alg)/len(times_third_alg)
    print("Average time for Ladder algorithm in milliseconds is %.5f" % (avg_time_first_alg * 1000))
    print("Average time for Binary search algorithm in milliseconds is %.5f" % (avg_time_second_alg * 1000))
    print("Average time for Ladder + Exponential search in milliseconds is %.5f" % (avg_time_third_alg * 1000))
    all_avg_times_first_alg.append(avg_time_first_alg)
    all_avg_times_second_alg.append(avg_time_second_alg)
    all_avg_times_third_alg.append(avg_time_third_alg)
    times_first_alg.clear()
    times_second_alg.clear()
    times_third_alg.clear()

plt.yscale("log")
plt.xscale("log")
plt.plot(n,all_avg_times_first_alg,label='Ladder')
plt.plot(n,all_avg_times_second_alg,label='Binary search')
plt.plot(n,all_avg_times_third_alg,label='Ladder + Exponential search')
plt.title('Algorithms of searching in matrix')
plt.xlabel('M size')
plt.ylabel('Time in seconds')
plt.legend()
plt.grid()
plt.show()