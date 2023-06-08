
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
