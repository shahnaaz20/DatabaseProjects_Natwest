import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='1234@snaaZ',auth_plugin='mysql_native_password',database="PayrollManagementSystem")

myacces =mydb.cursor()

# Creating table for employees basic detials
# myacces.execute("CREATE TABLE Employee_Details (Emp_id integer not null,Name text not null, address text not null,Contact integer not null,Father_Name text not null, Blood_Group text not null,Dept_id integer not null)")

# Creating table for employees daily attedence
# myacces.execute("CREATE TABLE Employee_Attendence(Name text not null, Date text not null ,In_Time text not null, Out_Time text not null,Dept_id integer not null,Salary integer not null)")

# Inserting the values 
# myacces.execute("insert into Employee_Attendence values('Deepa','19/2/2022','9:00','4:00',101,1000)")


# Deleting the rows 
# myacces.execute("DELETE FROM Employee_Attendence WHERE Name='Megha'")

# Showing the perticular data
# myacces.execute("select * from Employee_Attendence where Name = 'Bharti'")

# Counting the days for perticular person
# myacces.execute("SELECT COUNT(*) FROM Employee_Attendence WHERE Name = 'Sheetal'")
# myacces.execute("SELECT * FROM Employee_Attendence WHERE Dept_id=101 AND Name='Megha'")

# Inster column if needed
# myacces.execute("ALTER TABLE Employee_Attendence ADD Emp_id integer not null")


# Rename the table if needed
# myacces.execute("ALTER TABLE Employee_Details RENAME Employee_peronal_Details")

# Update the vlaues
# myacces.execute("UPDATE Employee_Attendence SET Date='20/3/2022' WHERE Name='Megha'")


# Calculating  the salary
# myacces.execute("SELECT Name, SUM(Salary) FROM Employee_Attendence GROUP BY Name")

# Sum of salary of a perticular person
# myacces.execute("SELECT SUM(Salary) FROM Employee_Attendence where Name='Megha' ")

for i in myacces:
    print(i)

mydb.commit()
