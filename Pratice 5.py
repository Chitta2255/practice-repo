#a list of roll numbers =[101,105,102,101,108,105,110]print all unique roll no in the list
#using list

roll_numbers = [101,105,102,101,108,105,110]
unique_numbers =[]

for roll in roll_numbers:
    if roll not in unique_numbers:
        unique_numbers.append(roll)
print(unique_numbers)

#using set

roll_numbers = [101,105,102,101,108,105,110]
unique_numbers = set(roll_numbers)
print(unique_numbers)

#in given employee record in tuple list we have to ask user for employee id to search the employee record.

employees=[(101,"Alice",55000),
           (102,"Bob",65000),
           (103,"Charlie",75000)]
search_id =int(input("Enter Employee ID: "))
for emp in employees:
    emp_id,emp_name,emp_salary=emp
    if search_id == emp_id:
        print("Found Name:",emp_name,",""Salary:",emp_salary)
