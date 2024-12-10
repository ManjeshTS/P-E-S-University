import csv
import os

# Keywords for analysis
positive_keywords = ["excellent", "great", "satisfied", "happy"]
negative_keywords = ["poor", "bad", "disappointed", "unsatisfied"]

# File names
input_file = "feedback.txt"
good_feedback_file = "good_feedback.txt"
bad_feedback_file = "bad_feedback.txt"
summary_file = "keyword_counts.csv"

# Initialize counters
keyword_counts = {word: 0 for word in positive_keywords + negative_keywords}
good_feedback_count = 0
bad_feedback_count = 0

# Read feedback and analyze
with open(input_file, "r") as file:
    feedback_lines = file.readlines()

good_feedback = []
bad_feedback = []

for line in feedback_lines:
    line_lower = line.lower()
    is_positive = any(word in line_lower for word in positive_keywords)
    is_negative = any(word in line_lower for word in negative_keywords)

    # Count keywords
    for word in positive_keywords + negative_keywords:
        keyword_counts[word] += line_lower.count(word)

    # Categorize feedback
    if is_positive and not is_negative:
        good_feedback.append(line)
        good_feedback_count += 1
    elif is_negative and not is_positive:
        bad_feedback.append(line)
        bad_feedback_count += 1

# Append good and bad feedback to respective files
with open(good_feedback_file, "a") as file:
    file.writelines(good_feedback)

with open(bad_feedback_file, "a") as file:
    file.writelines(bad_feedback)

# Append summary to CSV
file_exists = os.path.exists(summary_file)

with open(summary_file, "a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["Keyword", "Count"])  # Write header if file doesn't exist
    for keyword, count in keyword_counts.items():
        writer.writerow([keyword, count])

    # Write overall counts
    writer.writerow(["Good Feedback Lines", good_feedback_count])
    writer.writerow(["Bad Feedback Lines", bad_feedback_count])

print("Analysis complete. Files updated successfully.")