#!/usr/bin/env python
import sys

#python task1.py <textfile> <r1> <r2> (r3)
"""
r1 = ip or http
r2 = 1(count) or 2(percentage) or 3(total bytes)
r3 = number or blank
"""

#Function
def step1(r1,print_num):
    count=0
    count_list=[]
    first_list=[]
    bytes_list=[]
    trim_list=[]
    grouped_list=[]
    
    for i in range(0,len(init_list)):
        first_list.append(init_list[i][r1])
        bytes_list.append(init_list[i][9])

    grouped_list=sorted(zip(first_list,bytes_list))
    
    trim_list.append(first_list[0])
    for item1 in first_list:
        if item1 in trim_list:
            continue
        elif item1 not in trim_list:
            trim_list.append(item1)
    
    for item2 in trim_list:
        count=first_list.count(item2)
        count_list.append(count)
    step2(count_list,trim_list,grouped_list,print_num)

def step2(x,y,z,print_num):
    tot=0
    last_list=[]
    bytes_sum_list=[]
    r2=sys.argv[3]

    if print_num==-1 or print_num>len(y):
        print_num=len(y)

    if r2=="1":
        last_list=sorted(zip(x,y))
        for i in range(len(y)-1,len(y)-print_num-1,-1):
            print("TOP-",len(y)-i,"COUNT=",last_list[i][0]," - ",last_list[i][1])

    elif r2=="2":
        for num in x:
            tot+=num

        for i in range(0,len(x)):
            x[i]=x[i]*100/tot

        last_list=sorted(zip(x,y))
        for i in range(len(y)-1,len(y)-print_num-1,-1):
            print("TOP-",len(y)-i,"PERCENTAGE=",round(last_list[i][0],2),"%"," - ",last_list[i][1])

    elif r2=="3":
        for i in range(0,len(y)):
            bytes_sum=0
            for j in range(0,len(z)):
                if z[j][0]==y[i]:
                    if z[j][1] == "-":
                        continue
                    else:
                        bytes_sum+=int(z[j][1])
                else:
                    continue
            bytes_sum_list.append(bytes_sum)
        last_list=sorted(zip(bytes_sum_list,y))
        for i in range(len(y)-1,len(y)-print_num-1,-1):
            print("TOP-",len(y)-i,"Total Bytes=",int(last_list[i][0])," - ",last_list[i][1])
    else:
        sys.exit()

#MAIN
if __name__ == '__main__':
    init_list=[]

    try:
        if len(sys.argv) == 5:
            r3=sys.argv[4]
            print_num=int(r3)
            if print_num<=0 :
                sys.exit()
        elif len(sys.argv) == 4:
            print_num=-1
        else:
            sys.exit()

        filename = sys.argv[1]
        r1 = sys.argv[2]
        with open(filename, 'r') as logfile:
            for line in logfile:
                line = line.split(" ")
                init_list.append(line)

        if r1 == "ip":
            step1(0,print_num)

        elif r1 == "http":
            step1(8,print_num)
    
        else:
            sys.exit()

    except:
        print("ERROR")
