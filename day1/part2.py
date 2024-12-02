
def main():

    list1 = []
    dict2 = {}

    similarities = []

    with open('input.txt', 'r') as file:
        
        for line in file:
            arr = line.split('   ')
            list1.append(int(arr[0]))

            if (int(arr[1]) in dict2):
                dict2[int(arr[1])] = dict2.get(int(arr[1])) + 1
            else:
                dict2.setdefault(int(arr[1]), 1)

        print(list1)
        print('\n\n\n')
        print(dict2)
 
    for x in range(0, len(list1)):
        if x in dict2: 
            sim = dict2[x]
        else:
            sim = 0
        similarities.append(list1[x] * sim)



    print('distances:\n\n')

    print(similarities)

    sum = 0

    for x in similarities:
        sum += x

    print('sum:\n\n')

    print(sum)

if __name__ == '__main__':
    main()
