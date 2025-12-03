from Employee_System import *



my_company  = Company ("Aitronix")

hr_dep = Department( "HR" , "Ahmed Hafez ")
it_dep = Department ("IT" , "Sara khalid")

my_company.Add_department (hr_dep)
my_company.Add_department(it_dep)

print ("------------------")
emp1 = FullTimeEmployee("10001" , "Jamil yasser" , "2002-12-25" ,5000  , 0.14 )
emp2 = PartTimeEmployee("10003" , "Khalid Ahmed" , "2022-6-21" , 2000 , 150 , 160 )
emp3 = FullTimeEmployee("10004" , "Menna youssef " , "2006-2-2" , 3000 , 0.16)
print ("------------------")
my_company.Add_Employee(emp1 , "IT")
my_company.Add_Employee (emp2 , "HR")
my_company.Add_Employee (emp3 , "IT")
print ("------------------")
print (my_company.display_all_salarie())
print ("------------------")

print (hr_dep.Department_Details)

print (emp1.Calculate_Salary())





