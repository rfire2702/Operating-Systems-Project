import copy 

# first come first serve

def fcfs():
    l = []
    n = int(input('Enter number of processes:- '))
    print('Enter process no., arrival time and burst time')
    for i in range(n):
        x = list(map(int, input().split()))
        l.append(x)

    l.sort(key=lambda l: l[1])

    for i in range(n):
        y = 0
        for j in range(i + 1):
            if(j == 0):
                y += l[j][2] + l[j][1]
            else:
                y += l[j][2]
        l[i].append(y)

    for i in range(n):
        y = l[i][3] - l[i][1]
        l[i].append(y)
        z = l[i][4] - l[i][2]
        l[i].append(z)

    for i in range(n):
        if l[i][5] < 0:
            x = abs(l[i][5])
            for j in range(i, n):
                l[j][3] += x
                l[j][4] += x
                l[j][5] += x

    atat1 = 0
    awt1 = 0
    for i in range(n):
        atat1 += l[i][4]
        awt1 += l[i][5]
    atat = atat1 / n
    awt = awt1 / n

    process = []
    for i in range(n):
        if i == 0 and l[i][1] != 0:
            process.append(('idle', 0, l[i][1]))
            process.append((l[i][0], l[i][1], l[i][3]))
        elif l[i][1] > l[i-1][3]:
            process.append(('idle', l[i-1][3], l[i][1]))
            process.append((l[i][0], l[i][1], l[i][3]))
        else:
            process.append((l[i][0], l[i][1], l[i][3]))

    s = "|"
    for i in range(len(process)):
        s += "  " + str(process[i][0]) + "  |"
    s1 = "0"
    for i in range(len(process)):
        if process[i][0] == 'idle':
            s1 += "        " + str(process[i][2])
        else:
            s1 += "     " + str(process[i][2])

    l.sort()

    print("\nGantt Chart:")

    for i in range(len(s)):
        print("-", end='')
    print(end='\n')
    print(s)
    for i in range(len(s)):
        print("-", end='')
    print(end='\n')
    print(s1)

    print("\nTable:\n")

    print('Process No.\tArrival Time\tBurst time\tCompletion Time\t\tTurn Around Time\tWaiting Time \t')
    for i in range(n):
        print(l[i][0], '\t\t', l[i][1], '\t\t', l[i][2], '\t\t',
              l[i][3], '\t\t\t', l[i][4], '\t\t\t', l[i][5])
    print('\nAverage Waiting Time =', awt)
    print('Average Turn Around Time =', atat)


# shortest job first


def sjfnonpre():
    l = []
    n = int(input('Enter number of processes:- '))
    print('Enter process no., arrival time and burst time')
    for i in range(n):
        x = list(map(int, input().split()))
        l.append(x)

    l.sort(key=lambda l: l[1])

    flag = 0
    firstelement = 0
    for i in range(1, n):
        if l[i-1][1] == l[i][1]:
            flag = 1
        else:
            firstelement = i
            flag = 0
            break

    min = l[0][2]
    for i in range(firstelement):
        if l[i][2] < min:
            l[i], l[0] = l[0], l[i]
            min = l[i][2]

    btime = 0
    k = 1
    if flag == 1:
        l.sort(key=lambda l: l[2])
    else:
        for j in range(n - 1):
            if j == 0:
                btime += l[j][1] + l[j][2]
                min = l[k][2]
            else:
                btime += l[j][2]
                min = l[k][2]
            for i in range(k, n):
                if (btime >= l[i][1]) and (l[i][2] < min):
                    l[i], l[k] = l[k], l[i]
                    min = l[k][2]
            k += 1

    for i in range(n):
        y = 0
        for j in range(i + 1):
            if(j == 0):
                y += l[j][2] + l[j][1]
            else:
                y += l[j][2]
        l[i].append(y)

    for i in range(n):
        y = l[i][3] - l[i][1]
        l[i].append(y)
        z = l[i][4] - l[i][2]
        l[i].append(z)

    for i in range(n):
        if l[i][5] < 0:
            x = abs(l[i][5])
            for j in range(i, n):
                l[j][3] += x
                l[j][4] += x
                l[j][5] += x

    atat1 = 0
    awt1 = 0
    for i in range(n):
        atat1 += l[i][4]
        awt1 += l[i][5]
    atat = atat1 / n
    awt = awt1 / n

    process = []
    for i in range(n):
        if i == 0 and l[i][1] != 0:
            process.append(('idle', 0, l[i][1]))
            process.append((l[i][0], l[i][1], l[i][3]))
        elif l[i][1] > l[i-1][3]:
            process.append(('idle', l[i-1][3], l[i][1]))
            process.append((l[i][0], l[i][1], l[i][3]))
        else:
            process.append((l[i][0], l[i][1], l[i][3]))

    s = "|"
    for i in range(len(process)):
        s += "  " + str(process[i][0]) + "  |"
    s1 = "0"
    for i in range(len(process)):
        if process[i][0] == 'idle':
            s1 += "        " + str(process[i][2])
        else:
            s1 += "     " + str(process[i][2])

    l.sort()

    print("\nGantt Chart:")

    for i in range(len(s)):
        print("-", end='')
    print(end='\n')
    print(s)
    for i in range(len(s)):
        print("-", end='')
    print(end='\n')
    print(s1)

    print("\nTable:\n")

    print('Process No.\tArrival Time\tBurst time\tCompletion Time\t\tTurn Around Time\tWaiting Time \t')
    for i in range(n):
        print(l[i][0], '\t\t', l[i][1], '\t\t', l[i][2], '\t\t',
              l[i][3], '\t\t\t', l[i][4], '\t\t\t', l[i][5])
    print('\nAverage Waiting Time =', awt)
    print('Average Turn Around Time =', atat)


# shortest remaining time first


def srtf():
    p_info = []
    process_order = []

    # getting input from the user: processid, arrival time and burst time

    n = int(input('ENTER THE NUMBER OF PROCESSES: '))
    print('ENTER THE PROCESS ID, ARRIVAL TIME AND BURST TIME RESPECTIVELY: ')
    for _ in range(n):
       temp_list = list(map(int, input().split()))
       temp_list.append(0)
       p_info.append(temp_list)
    original_p_info = copy.deepcopy(p_info)

    # p_info contains all the information of a process
    # each list(process) of p_info has [processid, arrival time, burst time, completion time]

    # sorting on the basis of arrival time

    p_info.sort(key=lambda k: k[1])
    original_p_info.sort(key=lambda p: p[1])

    # current time in the gantt chart

    cur_time = 0

    # total time required for completion of all the jobs

    tot_time_req = 0
    for i in range(n):
        tot_time_req += p_info[i][2]

    counter = 0
    j = 0

    while(counter < tot_time_req):
        min_bt = 99999999
        p_no = None
        for j in range(n):
            if p_info[j][2] != 0:
                if p_info[j][1] <= cur_time:
                    if p_info[j][2] < min_bt:
                        min_bt = p_info[j][2]
                        p_no = p_info[j][0]
        if p_no is None:
            process_order.append(-1)
            cur_time += 1
        else:
            process_order.append(p_no)
            cur_time += 1
            counter += 1
            for k in range(n):
                if p_no == p_info[k][0]:
                    p_info[k][2] -= 1
                    p_info[k][3] = cur_time

    # preparing gantt chart

    gantt_chart = []
    i = 0
    ct = 0
    while i < len(process_order):
        x = 1
        for j in range(i + 1, len(process_order)):
            if process_order[i] == process_order[j]:
                x += 1
                if j == len(process_order) - 1:
                    ct += x
                    break
            else:
                ct += x
                break
        gantt_chart.append([process_order[i], ct])
        i += x

    # printing gantt chart

    print('\nGANTT CHART: ')
    for p in range(len(gantt_chart)):
        if gantt_chart[p][0] == -1:
            print('IDLE\t|', end='')
        else:
            print('P{}\t|'.format(gantt_chart[p][0]), end='')
    print()
    print('0', '\t', end='')
    for p in range(len(gantt_chart)):
        print(gantt_chart[p][1], '\t', end='')

    print()

    # sorting on the basis of process time

    p_info.sort(key=lambda k: k[0])
    original_p_info.sort(key=lambda p: p[0])

    print("\nTABLE:\n")

    print('PROCESS NO.\tARRIVAL TIME\tBURST TIME\tCOMPLETION TIME\t\tTURN AROUND TIME\tWAITING TIME\t')
    for i in range(n):
        print(original_p_info[i][0], '\t\t', original_p_info[i][1], '\t\t', original_p_info[i][2],
              '\t\t', p_info[i][3], '\t\t\t', p_info[i][3] - p_info[i][1], '\t\t\t\t', p_info[i][3] - p_info[i][1] - original_p_info[i][2])

    tot_tat = 0
    tot_wt = 0

    for i in range(n):
        tot_tat += p_info[i][3] - p_info[i][1]
        tot_wt += p_info[i][3] - p_info[i][1] - original_p_info[i][2]

    avg_tat = tot_tat / n
    avg_wt = tot_wt / n

    print('\nAVERAGE TURN AROUND TIME: ', avg_tat)
    print('AVERAGE WAITING TIME: ', avg_wt)


# priority(non-preemptive)

def prinonpre():
    l = []
    n = int(input('Enter number of processes:- '))
    print('Enter process no., arrival time and burst time and priority')
    for i in range(n):
        x = list(map(int, input().split()))
        l.append(x)

    l.sort(key=lambda l: l[1])

    flag = 0
    firstelement = 0
    for i in range(1, n):
        if l[i-1][1] == l[i][1]:
            flag = 1
        else:
            firstelement = i
            flag = 0
            break

    max = l[0][3]
    for i in range(firstelement):
        if l[i][3] > max:
            l[i], l[0] = l[0], l[i]
            max = l[i][3]

    btime = 0
    k = 1
    if flag == 1:
        l.sort(key=lambda l: l[3])
    else:
        for j in range(n - 1):
            if j == 0:
                btime += l[j][1] + l[j][2]
                max = l[k][3]
            else:
                btime += l[j][2]
                max = l[k][3]
            for i in range(k, n):
                if (btime >= l[i][1]) and (l[i][3] > max):
                    l[i], l[k] = l[k], l[i]
                    max = l[k][3]
            k += 1

    for i in range(n):
        y = 0
        for j in range(i + 1):
            if(j == 0):
                y += l[j][2] + l[j][1]
            else:
                y += l[j][2]
        l[i].append(y)

    for i in range(n):
        y = l[i][4] - l[i][1]
        l[i].append(y)
        z = l[i][5] - l[i][2]
        l[i].append(z)

    for i in range(n):
        if l[i][6] < 0:
            x = abs(l[i][6])
            for j in range(i, n):
                l[j][4] += x
                l[j][5] += x
                l[j][6] += x

    atat1 = 0
    awt1 = 0
    for i in range(n):
        atat1 += l[i][5]
        awt1 += l[i][6]
    atat = atat1 / n
    awt = awt1 / n

    process = []
    for i in range(n):
        if i == 0 and l[i][1] != 0:
            process.append(('idle', 0, l[i][1]))
            process.append((l[i][0], l[i][1], l[i][4]))
        elif l[i][1] > l[i-1][3]:
            process.append(('idle', l[i-1][4], l[i][1]))
            process.append((l[i][0], l[i][1], l[i][4]))
        else:
            process.append((l[i][0], l[i][1], l[i][4]))

    s = "|"
    for i in range(len(process)):
        s += "  " + str(process[i][0]) + "  |"
    s1 = "0"
    for i in range(len(process)):
        if process[i][0] == 'idle':
            s1 += "        " + str(process[i][2])
        else:
            s1 += "     " + str(process[i][2])

    l.sort()

    print("\nGantt Chart:")

    for i in range(len(s)):
        print("-", end='')
    print(end='\n')
    print(s)
    for i in range(len(s)):
        print("-", end='')
    print(end='\n')
    print(s1)

    print("\nTable:\n")

    print('Process No.\tArrival Time\tBurst time\tPriority\tCompletion Time\t\tTurn Around Time\tWaiting Time \t')
    for i in range(n):
        print(l[i][0], '\t\t', l[i][1], '\t\t', l[i][2], '\t\t', l[i]
              [3], '\t\t', l[i][4], '\t\t\t', l[i][5], '\t\t\t\t', l[i][6])
    print('\nAverage Waiting Time =', awt)
    print('Average Turn Around Time =', atat)


# priority(preemptive)


def pp():
    # zero is the lowest priority
    p_info = []
    process_order = []

    # getting input from the user: processid, arrival time, burst time and priority

    print('NOTE: 0 IS TAKEN AS THE LOWEST PRIORITY.')
    n = int(input('ENTER THE NUMBER OF PROCESSES: '))
    print('ENTER THE PROCESS ID, ARRIVAL TIME, BURST TIME AND PRIORITY RESPECTIVELY: ')
    for _ in range(n):
       temp_list = list(map(int, input().split()))
       temp_list.append(0)
       p_info.append(temp_list)

    original_p_info = copy.deepcopy(p_info)

    # p_info contains all the information of a process
    # each list(process) of p_info has [processid, arrival time, burst time, priority completion time]

    # sorting on the basis of arrival time

    p_info.sort(key=lambda k: k[1])
    original_p_info.sort(key=lambda p: p[1])

    # current time in the gantt chart

    cur_time = 0

    # total time required for completion of all the jobs

    tot_time_req = 0
    for i in range(n):
        tot_time_req += p_info[i][2]

    counter = 0
    j = 0

    while(counter < tot_time_req):
        max_pt = -1
        p_no = None
        for j in range(n):
            if p_info[j][2] != 0:
                if p_info[j][1] <= cur_time:
                    if p_info[j][3] > max_pt:
                        max_pt = p_info[j][3]
                        p_no = p_info[j][0]
        if p_no is None:
            process_order.append(-1)
            cur_time += 1
        else:
            process_order.append(p_no)
            cur_time += 1
            counter += 1
            for k in range(n):
                if p_no == p_info[k][0]:
                    p_info[k][2] -= 1
                    p_info[k][4] = cur_time

    # preparing gantt chart

    gantt_chart = []
    i = 0
    ct = 0
    while i < len(process_order):
        x = 1
        for j in range(i + 1, len(process_order)):
            if process_order[i] == process_order[j]:
                x += 1
                if j == len(process_order) - 1:
                    ct += x
                    break
            else:
                ct += x
                break
        gantt_chart.append([process_order[i], ct])
        i += x

    # printing gantt chart

    print('\nGANTT CHART: ')
    for p in range(len(gantt_chart)):
        if gantt_chart[p][0] == -1:
            print('IDLE\t|', end='')
        else:
            print('P{}\t|'.format(gantt_chart[p][0]), end='')
    print()
    print('0', '\t', end='')
    for p in range(len(gantt_chart)):
        print(gantt_chart[p][1], '\t', end='')

    # sorting on the basis of process time

    p_info.sort(key=lambda k: k[0])
    original_p_info.sort(key=lambda p: p[0])

    print("\n\nTABLE:\n")

    print('PROCESS NO.\tARRIVAL TIME\tBURST TIME\tPRIORITY\tCOMPLETION TIME\t\tTURN AROUND TIME\tWAITING TIME\t')
    for i in range(n):
        print(original_p_info[i][0], '\t\t', original_p_info[i][1], '\t\t', original_p_info[i][2],
              '\t\t', p_info[i][3], '\t\t', p_info[i][4], '\t\t\t', p_info[i][4] - p_info[i][1], '\t\t\t\t', p_info[i][4] - p_info[i][1] - original_p_info[i][2])

    tot_tat = 0
    tot_wt = 0

    for i in range(n):
        tot_tat += p_info[i][4] - p_info[i][1]
        tot_wt += p_info[i][4] - p_info[i][1] - original_p_info[i][2]

    avg_tat = tot_tat / n
    avg_wt = tot_wt / n

    print('\nAVERAGE TURN AROUND TIME: ', avg_tat)
    print('AVERAGE WAITING TIME: ', avg_wt)


# round robin 

def rr():
    p_info = []
    process_order = []
    completed = []

    time_quant = int(input('ENTER THE TIME QUANTUM: '))

    # getting input from the user: processid, arrival time and burst time

    n = int(input('ENTER THE NUMBER OF PROCESSES: '))
    print('ENTER THE PROCESS ID, ARRIVAL TIME AND BURST TIME RESPECTIVELY: ')
    for _ in range(n):
        temp_list = list(map(int, input().split()))
        temp_list.append(0)
        p_info.append(temp_list)
    original_p_info = copy.deepcopy(p_info)

    # original_p_info contains all the information of a process

    # sorting on the basis of arrival time

    p_info.sort(key=lambda k: k[1])
    original_p_info.sort(key=lambda p: p[1])
    # current time in the gantt chart

    cur_time = 0

    # total time required for completion of all the jobs

    tot_time_req = 0
    for i in range(n):
        tot_time_req += p_info[i][2]

    counter = 0

    while(counter < tot_time_req):
        p_no = None
        p_info.sort(key=lambda k: (k[1], k[0]))
        if p_info[0][2] != 0:
            if p_info[0][1] <= cur_time or int(p_info[0][1]) <= cur_time:
                p_no = p_info[0][0]
                if p_info[0][2] >= time_quant:
                    p_info[0][1] += time_quant + 0.0000000001

        if p_no is None:
            process_order.append(-1)
            cur_time += 1
        else:
            process_order.append(p_no)
            if p_info[0][2] >= time_quant:
                cur_time += time_quant
                counter += time_quant
            else:
                cur_time += p_info[0][2]
                counter += p_info[0][2]
            if p_info[0][2] >= time_quant:
                p_info[0][2] -= time_quant
            else:
                p_info[0][2] = 0
            p_info[0][3] = cur_time
            if p_info[0][2] == 0:
                completed.append(p_info[0])
                del p_info[0]

    # preparing gantt chart

    gantt_chart = []
    copy_p_info = copy.deepcopy(original_p_info)
    copy_p_info.sort(key=lambda p: p[0])
    i = 0
    while i < len(process_order):
        ct = 0
        x = 1
        for j in range(i + 1, len(process_order)):
            if process_order[i] == process_order[j]:
                x += 1
                if j == len(process_order) - 1:
                    ct += x
                    break
            else:
                ct += x
                break
        if i + 1 == len(process_order):
            ct = 1
        gantt_chart.append([process_order[i], ct])
        i += x

    gantt_time = []
    for p in range(len(gantt_chart)):
        if gantt_chart[p][0] == -1:
            gantt_time.append(gantt_chart[p][1])
        else:
            p_id = gantt_chart[p][0] - 1
            if copy_p_info[p_id][2] >= time_quant:
                gantt_time.append(gantt_chart[p][1] * time_quant)
                copy_p_info[p_id][2] -= time_quant
            else:
                gantt_time.append(copy_p_info[p_id][2])
                copy_p_info[p_id][2] = 0
    h = gantt_chart[-1][0] - 1
    for p in range(1, len(gantt_time)):
        gantt_time[p] += gantt_time[p - 1]
    completed.sort(key=lambda k: k[0])
    gantt_time[-1] = completed[h][3]

    # printing gantt chart

    print('\nGANTT CHART: ')
    for p in range(len(gantt_chart)):
        if gantt_chart[p][0] == -1:
            print('IDLE\t|', end='')
        else:
            print('P{}\t|'.format(gantt_chart[p][0]), end='')
    print()
    print('0', '\t', end='')
    for p in range(len(gantt_time)):
        print(gantt_time[p], '\t', end='')

    print()

    # sorting on the basis of process time

    completed.sort(key=lambda k: k[0])
    original_p_info.sort(key=lambda p: p[0])

    print("\nTABLE:\n")

    print('PROCESS NO.\tARRIVAL TIME\tBURST TIME\tCOMPLETION TIME\t\tTURN AROUND TIME\tWAITING TIME\t')
    for i in range(n):
        print(original_p_info[i][0], '\t\t', original_p_info[i][1], '\t\t', original_p_info[i][2],
              '\t\t', completed[i][3], '\t\t\t', completed[i][3] - original_p_info[i][1], '\t\t\t\t', completed[i][3] - original_p_info[i][1] - original_p_info[i][2])

    tot_tat = 0
    tot_wt = 0

    for i in range(n):
        tot_tat += completed[i][3] - original_p_info[i][1]
        tot_wt += completed[i][3] - \
            original_p_info[i][1] - original_p_info[i][2]

    avg_tat = tot_tat / n
    avg_wt = tot_wt / n

    print('\nAVERAGE TURN AROUND TIME: ', avg_tat)
    print('AVERAGE WAITING TIME: ', avg_wt)


# main


print('\nPREPARED BY: SIDDHANT CHANDRA KULSHRESTHA AND PREET MISHRA')
print('UNDER THE SUPERVISION OF: DR. MAINAK BANDYOPADHYAY\n')
print('OPERATING SYSTEM SCHEDULING ALGORITHMS: ')
while True :
    print('\nCHOOSE AN ALGORITHM FROM THE LIST: ')
    print('1. FIRST COME FIRST SERVE')
    print('2. SHORTEST JOB FIRST')
    print('3. SHORTEST REMAINING TIME FIRST')
    print('4. PRIORITY SCHEDULING(NON-PREEMPTIVE)')
    print('5. PRIORITY SCHEDULING(PREEMPTIVE)')
    print('6. ROUND ROBIN')
    print('ENTER ANY OTHER NUMBER TO EXIT')
    option = int (input())
    if option == 1 :
        fcfs()
    elif option == 2 :
        sjfnonpre()
    elif option == 3 :
        srtf()
    elif option == 4 :
        prinonpre()
    elif option == 5 :
        pp()
    elif option == 6 :
        rr()
    else :
        break