# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

toal_heights = 0

for n in student_heights:
  toal_heights = toal_heights + n

print(toal_heights)


toal_students = 0 

for n in student_heights:
  toal_students = toal_students + 1 

print(toal_students)

average_height = toal_heights/toal_students
print("Average height of the stidents is, ", average_height)