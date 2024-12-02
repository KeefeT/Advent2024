def main():
    count = 0
    reports = [] # 2d array reports[x] = list of levels for that report

    with open('input.txt', 'r') as file:
        for line in file:
            reports.append([int(x) for x in line.split(' ')])

    for report in reports:
        inc = False
        dec = False
        safe = False

        for x in range(0, len(report) - 1):
            print(x)
            if report[x] > report[x+1]:
                dec = True
            elif report[x] < report[x+1]:
                inc = True

            if dec == True and inc == True:
                #must only be increasing OR decreasing, not both
                print('INC/DEC fail, break')
                safe = False
                break

            if abs(report[x] - report[x+1]) >= 1 and abs(report[x] - report[x+1]) <= 3:
                print('x: %d, x+1: %d, diff: %d' % (report[x], report[x+1], abs(report[x] - report[x+1])))
                safe = True
            else:
                print('DIFF FAIL')
                safe = False
                break
        
        if safe == True:
            print('REPORT IS SAFE')
            count += 1

    print(count)

if __name__ == '__main__':
    main()