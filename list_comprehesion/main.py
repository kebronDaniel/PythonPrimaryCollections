#
# squared = [num for num in range(1,50) if num % 2 == 0]
# print(squared)
#
# new_names = [name[0:2] for name in names if len(name) > 3]
# print(new_names)

# with open("file1.txt") as file1, open("file2.txt") as file2:
#     first_data = file1.readlines()
#     second = file2.readlines()
#
# common = [int(number) for number in first_data if number in second]
# print(common)
import random

# names = ["Kebron", "sivan", "daniel", "naomi"]
# student_score = {name: random.randint(80, 100) for name in names}
# print(student_score)
# passed = {student:score for (student,score) in student_score.items() if score > 90}
# print(passed)

# sentence = "This is the sample sentence that was assigned to illustrate a dictionary comprehension"
# new_sentence = sentence.split(" ")
# word_count = {word:len(word) for word in new_sentence}
# print(word_count)

temperature = {
    "Monday": 34,
    "Tuesday": 21,
    "Wednesday": 10,
    "Thursday": 17,
    "Friday": 24,
    "Saturday": 50,
    "Sunday": 12,
}
new_temp = {day: ((value*9/5) + 32) for (day, value) in temperature.items()}
print(new_temp)