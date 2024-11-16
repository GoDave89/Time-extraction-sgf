import re
import csv

def main():
    with open('sgfdoc.txt') as file:
        sgfdoc = file.read()

    numbers = re.findall(r'-?\d+\.?\d*', sgfdoc)
    numeric_values = [float(num) if '.' in num else int(num) for num in numbers] 
    
    only_times = [item for item in numeric_values if isinstance(item, float)]

    time_used = [3600-item for item in only_times]

    only_b_times = []
    only_w_times = []

    for i in range (0, len(time_used)):
        if i%2 == 0:
            if i < 2:
                only_b_times.append(time_used[i])
            else:
                only_b_times.append(time_used[i]-time_used[i-2])
        if i%2 == 1:
            if i < 2:
                only_w_times.append(time_used[i])
            else:
                only_w_times.append(time_used[i]-time_used[i-2])
           
    int_obt = [int(item) for item in only_b_times]
    int_owt = [int(item) for item in only_w_times]

    int_obt_mod = [item + 300 if item<0 else item for item in int_obt]
    int_owt_mod = [item + 300 if item<0 else item for item in int_owt]

    with open('sorted_times.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for item1, item2 in zip(int_obt_mod, int_owt_mod):
            writer.writerow([item1,item2])

    
   




if __name__ == "__main__":
    main()