l =[]

def usr_entry(i):

    x = float(input(f"Enter rainfall for month {i}"))
    if int(x)>0:
        l.append(x)
        return
        
    else:
        usr_entry(i)
    


for i in range(1,12):
    usr_entry(i)
    




print(f"Total: {sum(l)}")
print(f"Average: {sum(l)/len(l)}")
print(f"Highest: {max(l)}")
print(f"lowest: {min(l)}")
