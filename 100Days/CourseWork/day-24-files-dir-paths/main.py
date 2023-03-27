
file_path = "CourseWork/day-24-files-dir-paths/my_txt_file.txt"

# To READ contents within the file
with open(file_path) as file:
    txt = file.read()

# To WRITE contents into the file
#   Will replace contents w/in file with whatever you write to it
#
# with open(file_path, mode="w") as file:
#     file.read("Test test")

# To ADD contents into the file
#   Will APPEND contents into file with whatever you write to it
#
with open(file_path, mode="a") as file:
    file.write("\nTest test")

print(txt)
