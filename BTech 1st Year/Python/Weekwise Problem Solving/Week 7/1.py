#1
        
import csv

def department_with_highest_experience(file_path):
    # Dictionary to store experience totals and counts for each department
    department_experience = {}
    
    # Read the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            department = row['Department']
            years_of_experience = float(row['Years_of_Experience'])
            
            if department not in department_experience:
                department_experience[department] = [0, 0]  # [total_experience, count]
            
            # Update total experience and count for the department
            department_experience[department][0] += years_of_experience
            department_experience[department][1] += 1
    
    # Calculate the department with the highest average experience
    highest_avg_experience = 0
    top_department = None
    
    for department, (total_experience, count) in department_experience.items():
        avg_experience = total_experience / count
        if avg_experience > highest_avg_experience:
            highest_avg_experience = avg_experience
            top_department = department
    
    return top_department, highest_avg_experience


result = department_with_highest_experience("employees.csv")

print(result)

#2

import csv

def salary_by_age_group(file_path):
    # Define age groups
    age_groups = {
        '20-30': 0,
        '31-40': 0,
        '41-50': 0,
        '51-60': 0,
        '61+': 0
    }
    
    # Read the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            age = int(row['Age'])
            salary = float(row['Salary'])
            
            # Determine the age group
            if 20 <= age <= 30:
                age_groups['20-30'] += salary
            elif 31 <= age <= 40:
                age_groups['31-40'] += salary
            elif 41 <= age <= 50:
                age_groups['41-50'] += salary
            elif 51 <= age <= 60:
                age_groups['51-60'] += salary
            elif age > 60:
                age_groups['61+'] += salary
    
    return age_groups

file_path= "employees.csv"
result2= salary_by_age_group(file_path)
print(result2)

#3

import csv

def employees_above_average_salary(file_path):
    # Dictionaries to store total salary and count of employees per department
    department_salary = {}
    department_count = {}
    
    # First pass: Calculate total salary and count of employees for each department
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            department = row['Department']
            salary = float(row['Salary'])
            
            if department not in department_salary:
                department_salary[department] = 0
                department_count[department] = 0
            
            department_salary[department] += salary
            department_count[department] += 1
    
    # Calculate average salary for each department
    department_avg_salary = {
        department: department_salary[department] / department_count[department]
        for department in department_salary
    }
    
    # Second pass: Find employees with salary above their department's average
    employees = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            department = row['Department']
            salary = float(row['Salary'])
            name = row['Name']
            
            if salary > department_avg_salary[department]:
                employees.append(name)
    
    return employees

result3 = employees_above_average_salary(file_path)
print(result3)

#4
import csv

def give_raises(file_path):
    updated_rows = []
    
    # Read the CSV file and update salaries
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames  # Get the column headers
        
        for row in reader:
            years_of_experience = float(row['Years_of_Experience'])
            
            # Check if the employee has more than 5 years of experience
            if years_of_experience > 5:
                row['Salary'] = str(float(row['Salary']) * 1.10)  # Increase salary by 10%
            
            updated_rows.append(row)
    
    # Write the updated data back to the CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the headers
        writer.writerows(updated_rows)  # Write the updated rows

    print("Salaries updated successfully.")
    
result4= give_raises(file_path)
print(result4)