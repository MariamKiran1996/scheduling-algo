array = []
wait_sum = 0.0
waiting_time = []
service_time = []
turnaround_time = []
process_number = int(input('Enter the number of processes : '))

for i in range(process_number):
    array.append([])
    array[i].append(input('Process Name : ' ))
    array[i].append(int(input('Process Arrival Time ')))
    array[i].append(int(input('Process Burst Time :')))
    print('\n')

array.sort(key=lambda array:array[2])

j = 1
service_time.append(0)
waiting_time.append(service_time[0] + array[0][1])
turnaround_time.append(waiting_time[0]+array[0][2])

while j < process_number:
    service_time.append(service_time[j-1] + array[j-1][2])
    waiting_time.append(service_time[j] - array[j][1])
    turnaround_time.append(waiting_time[j] + array[j][2])
    j += 1

print ('Process Name \tArrival Time \t Burst Time \t Waiting Time \t Turn_around time')
for i in range(process_number):
    print (array[i][0], '\t\t\t\t', array[i][1],'\t\t\t\t', array[i][2], '\t\t\t\t',waiting_time[i], '\t\t\t\t', turnaround_time[i])
    wait_sum += waiting_time[i]

print('Average Waiting Time : ',(wait_sum/(process_number*1.0)))
