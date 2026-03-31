def read_input_from_file(filepath): # read input helper function
    with open(filepath, 'r') as f:
        data = f.read().split('\n')
    idx = 0

    K = int(data[idx]); idx += 1

    char_values = {}
    for _ in range(K):
        parts = data[idx].split(); idx += 1
        char_values[parts[0]] = int(parts[1])

    A = data[idx]; idx += 1
    B = data[idx]; idx += 1

    return K, char_values, A, B


def main():
    # print("Hello from pa3!")
    K, char_values, A, B = read_input_from_file("input.txt")
    print(f"K = {K}")
    print(f"char_values = {char_values}")
    print(f"A = {A}")
    print(f"B = {B}")

if __name__ == "__main__":
    main()
