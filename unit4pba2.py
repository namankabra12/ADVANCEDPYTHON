import pandas as pd 
import matplotlib.pyplot as plt 

try:
    df = pd.read_csv('employee.csv')
except FileNotFoundError:
    print("File Employee.csv not found!!")


print("------Employee Details------")
print(df[['name','department','salary']])
print('\n')

print("-----Average Salary per Department-------")
avg_salary = df.groupby("department")['salary'].mean()

avg_salary.plot(kind= 'bar' , color = 'skyblue' , edgecolor = 'black')

plt.title("average salary of employees")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()