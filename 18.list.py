def get_data():
    num_list=[]
    for i in range(1,7):
        a=int(input(f"Enter number {i}: "))
        num_list.append(a)
        
    return num_list

def low_num(num_list):
    return min(num_list)

def high_num(num_list):
    return max(num_list)

def total_num(num_list):
    return sum(num_list)

def avg_num(num_list):
    avg = sum(num_list)/len(num_list)
    return avg

def main():
    num_l = get_data()

    min_num = low_num(num_l)
    max_num = high_num(num_l)
    sum_num = total_num(num_l)
    average_num = avg_num(num_l)


    print(f"Lowest number: {min_num}")
    print(f"Highest number: {max_num}")
    print(f"Total of the numbers: {sum_num}")
    print(f"Average of the numbers: {average_num}")

main()
    
        
