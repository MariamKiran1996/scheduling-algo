arr = []
wait_time = 0
n = int(input('Enter the No. of Process : '))

for i in range(n):
    arr.append([])
    print(' ')
    arr[i].append(input('Enter Process Name : ' ))
    arr[i].append(int(input('Enter Arrival Time :')))
    arr[i].append(int(input('Enter Burst Time :')))


time_slice = int(input('Enter the time slice for each Process : '))

arr.sort(key = lambda arr:(arr[1],arr[n]))

total = 0
wait = []
finish = []
dup = []

for i in range(n):
    finish.append(0)
    total += arr[i][2]
    dup.append(arr[i][2])
    wait.append(0)


j = 0
l = 0

while (l<total):
    j = j % n
    for k in range(time_slice):
        if dup[j] != 0:
            dup[j] -= 1
            l += 1
            if dup[j] == 0:
                finish[j] = l + arr[j][1]
                break
    j += 1

for i in range(n):
    wait[i] = finish[i] - arr[i][1] - arr[i][2]

print ('Process Name \tArrival Time \t Burst Time \t  Waiting Time')
for i in range(n):
    print (arr[i][0], '\t\t\t\t', arr[i][1], '\t\t\t\t', arr[i][2], '\t\t\t\t', wait[i])
    wait_time += wait[i]

print ('Total Waiting Time : ',wait_time)
print ('Average Waiting Time : ',(wait_time/n))