
def main():

    list1 = []
    dict2 = {}

    similarities = []

    with open('input.txt', 'r') as file:
        
        for line in file:
            arr = line.split('   ')
            list1.append(int(arr[0]))

            arr[1] = int(arr[1])
            #print('adding %d to dict' % (arr[1]))

            if (arr[1] in dict2):
                #print('%d is in dict, current value is %d' % (arr[1], dict2.get(arr[1])) )
                dict2[arr[1]] = dict2.get(arr[1]) + 1
                #print('new count of %d is %d' % (arr[1], dict2.get(arr[1])))
            else:
                #print('%d is not in dict, setting to 1' % (arr[1]))
                dict2.setdefault(arr[1], 1)

            #print('\n')

        print(list1)
        print('\n\n\n')
        print(dict2)
 
    for x in range(0, len(list1)):
        sim = dict2.get(list1[x], 0)
        
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
