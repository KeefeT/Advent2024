import re

def main():

    matches = []
    sum = 0

    with open('input.txt', 'r') as file:

        for line in file:
            matches += re.findall(r"mul[(]\d{1,3},\d{1,3}[)]", line)

    for match in matches:
        ops = re.findall(r"\d{1,3}", match)
        sum += (int(ops[0]) * int(ops[1]))

    print(sum)

if __name__ == '__main__':
    main()