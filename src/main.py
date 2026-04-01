# TODO: add way to pick file like in past assignments
import time
import matplotlib.pyplot as plt

start = time.time()

def read_input_from_file(filepath):  # read input helper function
    with open(filepath, "r") as f:
        data = f.read().split("\n")
    idx = 0

    K = int(data[idx])
    idx += 1

    char_values = {}
    for _ in range(K):
        parts = data[idx].split()
        idx += 1
        char_values[parts[0]] = int(parts[1])

    A = data[idx]
    idx += 1
    B = data[idx]
    idx += 1

    return K, char_values, A, B


def main():
    K, char_values, A, B = read_input_from_file("assets/input10.txt")
    # print(f"K = {K}")
    # print(f"char_values = {char_values}")
    # print(f"A = {A}")
    # print(f"B = {B}")
    calculate(K, char_values, A, B)
    end = time.time()
    print(f"Runtime: {end - start:.6f} seconds")
    graph()

def calculate(K, char_values, A, B):
    n = len(A)
    m = len(B)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # literally just a recurrence relation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                # match: include me
                dp[i][j] = dp[i - 1][j - 1] + char_values[A[i - 1]]
            else:
                # no match: max stuff
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtrack
    result: list[str] = []
    i, j = n, m
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            # part of opt soln
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # reverse order
    result.reverse()

    # result
    print(dp[n][m])
    print(str("".join(result)))

def graph():
    input_files = [f"input{i}.txt" for i in range(1, 11)]
    runtimes = [0.000164, 0.000168, 0.000195, 0.000199, 0.000191,
                0.0002, 0.000219, 0.000250, 0.000244, 0.000363]
    plt.figure(figsize=(10, 5))
    plt.plot(input_files, runtimes, marker='o', color='blue', linewidth=2)
    # labels
    plt.xlabel("Input File")
    plt.ylabel("Runtime (seconds)")
    plt.title("HVLCS Runtime Across 10 Input Files")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("assets/runtime_graph.png")
    plt.show()

if __name__ == "__main__":
    main()
