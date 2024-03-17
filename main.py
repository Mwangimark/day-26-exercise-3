


with open("file1.txt") as file_1:
  file_1_contents = file_1.readlines()

with open("file2.txt") as file_2:
  file_2_contents = file_2.readlines()

result = [int(n)  for n in file_1_contents if n in file_2_contents]
# result = new_result.strip("\,n")


# Write your code above 👆

print(result)


