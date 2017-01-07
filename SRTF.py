arr = []
wait_time = 0
n = int(input('Enter the No. of Process : '))

for i in range(n):
    arr.append([])
    #print (' ')
    arr[i].append(input('Enter Process Name : ' ))
    arr[i].append(int(input('Enter Arrival Time ')))
    arr[i].append(int(input('Enter Burst Time :')))
    #print(' ')


arr.sort(key = lambda arr:(arr[1],arr[2]))


total = 0
for i in range(n):
    total += arr[i][2]

wait = []
j = 0
service = []
service[0]=0
service[1]=0

while (j<=total):
    service.append ( service[j] + arr[j][2] )
    wait.append(service[j] - arr[j][1])
    wait_time += wait[j]
    j += 1

print ('Process Name \tArrival Time \t Burst Time  \t Waiting Time')
for i in range(n):
    print(arr[i][0], '\t\t\t\t', arr[i][1], '\t\t\t\t', arr[i][2], '\t\t\t\t', wait[i])

print ('Total Waiting Time : ',wait_time)
print ('Average Waiting Time : ',(wait_time/n))