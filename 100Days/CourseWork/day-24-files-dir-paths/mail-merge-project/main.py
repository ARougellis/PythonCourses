# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_rel_path = "Input/Names/invited_names.txt"
names_abs_path = "/Users/arougellis/Desktop/PythonCourse/100Days/CourseWork/day-24-files-dir-paths/mail-merge-project/Input/Names/invited_names.txt"

letter_rel_path = "Input/Letters/starting_letter.txt"
letter_abs_path = "/Users/arougellis/Desktop/PythonCourse/100Days/CourseWork/day-24-files-dir-paths/mail-merge-project/Input/Letters/starting_letter.txt"

dest_rel_path = "Output/ReadyToSend"
dest_abs_path = "/Users/arougellis/Desktop/PythonCourse/100Days/CourseWork/day-24-files-dir-paths/mail-merge-project/Outout/ReadyToSend"

# Read the file of names into a list
with open(names_abs_path) as name_file:
    names = name_file.read().splitlines()

# Read invitation template into a variable and write names into invitation
with open(letter_abs_path) as invitation_file:
    invitation = invitation_file.read()
    for name in names:
        new_letter = invitation.replace("[name]", name)
        with open(f"/Users/arougellis/Desktop/PythonCourse/100Days/CourseWork/day-24-files-dir-paths/mail-merge-project/Outout/ReadyToSend/invitation_for_{name}", mode="w") as completed_letter:
        # with open(f"Output/ReadyToSend/invitation_for_{name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)
