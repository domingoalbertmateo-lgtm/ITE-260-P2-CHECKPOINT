def calculate_average(activity1, activity2, activity3):
    average = (activity1 + activity2 + activity3) / 3
    return average


num_students = int(input("How many students?: "))

for i in range(1, 4):
    print("Student", i)

    name = input("Enter name: ")

    activity1 = float(input("Enter score for activity 1: "))
    activity2 = float(input("Enter score for activity 2: "))
    activity3 = float(input("Enter score for activity 3: "))

    average = calculate_average(activity1, activity2, activity3)
    print("Average", average)


    if average >= 90:
        print("Excellent")
    elif average >= 80:
        print("Very Good")
    elif average >= 75:
        print("Passed")
    else:
        print("Failed")

 
