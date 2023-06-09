
# CATCHING EXCEPTIONS
#
# try:
#     mock_file = open("mock_file.txt")
#
#     mock_dict = {"key": "value"}
#     print(mock_dict["nonexistent_key"])
# except FileNotFoundError:
#     mock_file = open("mock_file.txt", "w")
#     mock_file.write("something")
# except KeyError as key_error_message:
#     print(f"The key {key_error_message} does not exist")
# else:
#     mock_file_content = mock_file.read()
#     print(mock_file_content)
# finally:
#     mock_file.close()
#     print("Mock file was closed")


# RAISING EXCEPTIONS
#
# Will raise an error if I think user inputted incorrectly
height = float(input("Height (in m): "))
weight = float(input("Weight (in kg): "))

if height > 4:
    raise ValueError("Human height typically isn't greater than 4m")

bmi = (weight/height)**2
print(bmi)


# ___EXAMPLE 1___: IndexError
#
# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)


# ___EXAMPLE 2___: KeyError
#
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         total_likes += 0
#
#
# print(total_likes)
