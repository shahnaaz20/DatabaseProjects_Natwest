import mysql.connector
from numpy import insert

mydb = mysql.connector.connect(host='localhost',user='root',password='1234@snaaZ',auth_plugin='mysql_native_password',database="RestaurantManagement")

myacces =mydb.cursor()

# Creating table for employees basic detials
# myacces.execute("CREATE TABLE Delivery_boys_details (Emp_id integer not null,Name text not null, address text not null,Contact integer not null,Alt_Contact integer not null,Father_Name text not null, Blood_Group text not null, Age integer not null)")

# Insering the  values
# myacces.execute("insert into Delivery_boys_details values(105,'salman','Delhi-sector 51',1221,2021,'Amair','O+', 28)")


# Create the menu chart
# myacces.execute("CREATE TABLE Menu_Chart(Food_Name text not null,Category text not null,Food_Type text not null,Cust_Rating float not null,Price integer not null)")

# insert the item in menu
# myacces.execute("insert into Menu_Chart values (Daal Makhni,South Indian , Veg , 4.0,200)")


# filetring the menu
# myacces.execute("SELECT * FROM Menu_Chart WHERE Category='South_Indian' AND price <= 150")

# deleting the menu item
# myacces.execute("DELETE FROM Menu_Chart WHERE Food_Name='Dosa'")

# myacces.execute("select * from Delivery_boys_details")
for i in myacces:
    print(i)

mydb.commit()