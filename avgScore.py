# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum=0
# Write your code below this row 👇

for x in student_heights:
  sum += x
avrg=round(sum/len(student_heights))
print(f"total height = {sum}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {avrg}")