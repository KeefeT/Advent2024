


def main():

    list1 = []
    list2 = []

    distances = []

    with open('input.txt', 'r') as file:
        
        for line in file:
            arr = line.split('   ')
            list1.append(int(arr[0]))

            list2.append(int(arr[1]))

        list1.sort()
        list2.sort()

        print(list1)
        print(list2)
 
    for x in range(0, len(list1)):
        distances.append(abs(list1[x] - list2[x]))



    print('distances:\n\n')

    print(distances)

    sum = 0

    for x in distances:
        sum += x

    print('sum:\n\n')

    print(sum)



if __name__ == '__main__':
    main()