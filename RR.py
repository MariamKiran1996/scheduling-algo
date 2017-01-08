array = []
wait_sum = 0.0
total_burst_time = 0
waiting_time = []
finish_time = []
burst_time_counter = []
turnaround_time=[]

process_number = int(input('Enter the number of processes : '))

for i in range(process_number):
    array.append([])
    array[i].append(input('Process Name : ' ))
    array[i].append(int(input('Process Arrival Time :')))
    array[i].append(int(input('process Burst Time :')))
    print('\n')

time_slice = int(input('Enter the time quantum for each process : '))
array .sort(key = lambda array :(array [1],array [process_number]))

for i in range(process_number):
    finish_time.append(0)
    total_burst_time += array [i][2]
    burst_time_counter.append(array [i][2])
    waiting_time.append(0)

j = 0
l = 0

while (l<total):
    j = j % process_number
    for k in range(time_slice):
        if burst_time_counter[j] != 0:
            burst_time_counter[j] -= 1
            l += 1
            if burst_time_counter[j] == 0:
                finish_time[j] = l + array [j][1]
                break
    j += 1

for i in range(process_number):
    waiting_time[i] = finish_time[i] - array[i][1] - array[i][2]
    turnaround_time.append(waiting_time[i]+array[i][2])

print ('Process Name \tArrival Time \t Burst Time \t  Waiting Time \t TurnAround Time')
for i in range(process_number):
    print (array[i][0], '\t\t\t\t', array[i][1], '\t\t\t\t', array[i][2], '\t\t\t\t', waiting_time[i], '\t\t\t\t', turnaround_time[i])
    wait_sum += waiting_time[i]

print ('Average Waiting Time : ',(wait_sum/(process_number*1.0)))
