# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#Write your code below this row 👇
print(student_heights)

total = 0 

for n in student_heights:
  total += n 
  print(total)

count = len(student_heights)
print(count)

Average = total/count
print(Average)