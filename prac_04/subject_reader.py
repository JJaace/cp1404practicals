"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_lecturer_info(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(",")
        data.append({"subject": parts[0], "lecturer": parts[1], "num_students": int(parts[2])})
    input_file.close()
    return data


def display_lecturer_info(data):
    """Display subject details."""
    for subject_info in data:
        print(f"{subject_info['subject']} is taught by {subject_info['lecturer']} "
              f"and has {subject_info['num_students']} students")


main()
