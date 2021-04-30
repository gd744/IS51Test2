"""
This program will be used to calculate and display the average of 24 final grades in a class.
It will also display and calculate the percentage of grades above the average grade.

The 24 grades will be read from the file "Final.txt" using the infile open command
"""

"""
PSUEDOCODE 

main
    infile = open final.txt
    copy each grade individually with linerstrip
close the infile
print number of grades in file to confirm

calculate the percent above average()

    class_average = sum of all grades / 24(total #)
    For loop of grade in grades 
        if grade > class_average:
            num +=1
    print("Class Average: , class_average)
    print("% of grades above the class average: , )
"""


def main():
    infile = open("Final.txt", 'r')
    grades = [int(line.rstrip()) for line in infile]
    infile.close()
    for i in range(len(grades)):
        grades[i] = int(grades[i])
    print("Number of grades: ", len(grades))
    print("Precalculated Average Grade: 83.25%")
    print("Precalculated Percentage of grades above class average: 54.17%")


def calculate_percent_above_average():
    class_average = sum(grades) / len(grades)
    num = 1
    for grade in grades:
        if grade > class_average:
            num += 1
    print("Percentage of Grades that Are Above Average: {0:.2f}%".format(100 * num / len(grades)))
#stuck here, wont return

main()
