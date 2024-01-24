#Function for calculating average

def calc_average(score):
    avg = sum(score)/len(score)
    print(avg)

def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >80:
        return "B"
    elif score >70:
        return "C"
    elif score >60:
        return "D"
    else:
        return "F"

def main():
    score = []

    for i in range(1,6):
        s = int(input(f"Enter your test score {i}: "))
        score.append(s)

    for j in score:
        print(f"{j}\t{determine_grade(j)}")



    print("Total Average Score is: ",calc_average(score))

main()

