from Employee_System.Department import Department
from Employee_System.Employee import Employee


class Company :
  def __init__ (self , name :str) : 
    self._company_name = name 
    self._all_departments = [] 
    self._all_employees = []

  def Add_department (self , dept : Department ) : 
    self._all_departments.append( dept)
    print ( f'Added a new Department {dept.department_name} successful ')


  def Add_Employee (self , emp : Employee , department_name : str ) : 
    target_dept = next ((dept for dept in self._all_departments if dept.department_name == department_name) , None )

    if target_dept: 
      self._all_employees.append (emp)
      target_dept.add_new_employee ( emp )
      print (f"Employee {emp.Employee_FullName()} added to  {department_name}")
    else : 
      print ("Error")

  def display_all_salarie (self) : 
    print ("Salary Report")
    report = []
    for emp in self._all_employees: 
      salary = emp.Calculate_Salary()
      report.append(f"{emp.Employee_FullName()} ( {type(emp).__name__}) : {salary:,.2f} EGP")
    return "\n".join (report)
