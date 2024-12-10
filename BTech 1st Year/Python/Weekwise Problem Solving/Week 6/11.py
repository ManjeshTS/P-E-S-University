# Dictionary storing feedback themes and corresponding feedback messages
feedback = {
    "Work Environment": ["Great work culture", "Need more team activities"],
    "Salary": ["Fair pay, but bonuses are inconsistent"],
    "Management": ["Leadership can improve", "Need more transparency"],
}

# Function to add new feedback to the relevant theme
def add_feedback(theme, message):
    if theme in feedback:
        feedback[theme].append(message)
    else:
        feedback[theme] = [message]

# Function to identify the theme with the most feedback
def theme_with_most_feedback(feedback_dict):
    max_theme = None
    max_count = 0
    for theme, messages in feedback_dict.items():
        if len(messages) > max_count:
            max_count = len(messages)
            max_theme = theme
    return max_theme, max_count

# Example usage
# Adding new feedback
add_feedback("Work Environment", "More flexible work hours")
add_feedback("Salary", "Increase in base salary would be great")

# Identifying the theme with the most feedback
theme, count = theme_with_most_feedback(feedback)
print(f"The theme with the most feedback is '{theme}' with {count} feedback messages.")