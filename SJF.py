arr = []
wait_time = 0
n = int(input('Enter the No. of Process : '))

for i in range(n):
    arr.append([])

    arr[i].append(input('Enter Process Name : ' ))
    arr[i].append(int(input('Enter Arrival Time ')))
    arr[i].append(int(input('Enter Burst Time :')))

arr.sort(key=lambda arr:arr[2])

wait = []
j = 1
service = []
service.append(0)
turn_around = []

wait.append(service[0] + arr[0][1])
turn_around.append(wait[0]+arr[0][2])

while j < n:
    service.append(service[j-1] + arr[j-1][2])
    wait.append(service[j] - arr[j][1])
    turn_around.append(wait[j] + arr[j-1][2])
    j += 1

print ('Process Name \tArrival Time \t Burst Time \t Waiting Time \t Turn_around time')
for i in range(n):
    print (arr[i][0] ,'\t\t\t\t' ,arr[i][1] ,'\t\t\t\t', arr[i][2], '\t\t\t\t',wait[i], '\t\t\t\t',turn_around[i])
    wait_time += wait[i]

print('Total Waiting Time : ',wait_time)
print('Average Waiting Time : ',(wait_time/n))