import os

def grade_student_files(key_file, student_folder, output_file):
    # Open the key file and read its content
    with open(key_file, 'r') as kf:
        key_lines = kf.readlines()

    # Prepare to write the results
    results = []

    # Iterate through each student file in the folder
    for student_file in os.listdir(student_folder):
        if student_file.endswith(".txt"):  # Ensure we process only text files
            student_path = os.path.join(student_folder, student_file)
            with open(student_path, 'r') as sf:
                student_lines = sf.readlines()

            # Calculate the score for the student
            score = 0
            for i, (key_line, student_line) in enumerate(zip(key_lines, student_lines)):
                if key_line.strip() == student_line.strip():  # Compare line by line
                    score += 2

            # Append the result for the student
            student_name = os.path.splitext(student_file)[0]
            results.append((student_name, score))

    # Write the results to the output file
    with open(output_file, 'w') as of:
        of.write("Student,Score\n")
        for student_name, score in results:
            of.write(f"{student_name},{score}\n")

    print(f"Grading complete. Results saved in {output_file}.")

# Specify the file paths and folder
key_output_file = "key_output.txt"
student_output_folder = "student_outputs"
results_output_file = "grading_results.csv"

# Grade the student files
grade_student_files(key_output_file, student_output_folder, results_output_file)