from Employee_System.Employee import Employee

class Department : 
  def __init__ (self , name : str  , manager : str ) : 
    self._Department_name = name
    self._manager = manager
    self.__employees = []  # List to hold employees in the department

  @property
  def Department_Details (self) -> str : 
    return f"Department Name : {self._Department_name} \nManager : {self._manager}"
    
  def add_new_employee (self , employee : Employee) : 
    self.__employees.append(employee)

  def department_employees (self) -> list : 
    return [emp.Employee_FullName() for emp in self.__employees]
  
  @property
  def department_name (self) : 
    return self._Department_name