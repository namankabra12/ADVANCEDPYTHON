def count_lines(path):
    with open(path, "r") as f:
        return sum(1 for _ in f)


def extract_first_lines(path, n):
    lines = []
    with open(path, "r") as f:
        for i, line in enumerate(f):
            if i == n:
                break
            lines.append(line)
    return lines


def write_lines(path, lines):
    with open(path, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    input_path = "input.txt"
    output_path = "output_first_two_lines.txt"

    total = count_lines(input_path)
    print("Total lines in file:", total)

    first_two = extract_first_lines(input_path, 2)
    print("First two lines:")
    for line in first_two:
        print(line.strip())

    write_lines(output_path, first_two)
    print("Written to", output_path)