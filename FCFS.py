arr = []
wait_time = 0.0
n = int(input('Enter the No. of Process : '))

for i in range(n):
    arr.append([])
    print (' ')
    arr[i].append(input('Enter Process Name : ' ))
    arr[i].append(int(input('Enter Arrival Time ')))
    arr[i].append(int(input('Enter Burst Time :')))
    print (' ')


arr.sort(key=lambda arr:arr[1])

wait = []
j = 1
service = []
service.append(arr[0][1])
wait.append(service[0] - arr[0][1])


while j < n:
    service.append(service[j-1] + arr[j-1][2])
    if service[j] < arr[j][1]:
        wait.append(0)
    else:
        wait.append(service[j] - arr[j][1])
    wait_time += wait[j]
    j += 1

print ('Process Name \tArrival Time \t Burst Time \t Service Time \t Waiting Time')
for i in range(n):
    print (arr[i][0], '\t\t\t\t', arr[i][1], '\t\t\t\t', arr[i][2], '\t\t\t\t', service[i], '\t\t\t\t', wait[i])

print ('Total Waiting Time : ', wait_time)
print ('Average Waiting Time : ', (wait_time/(n*1.0)))