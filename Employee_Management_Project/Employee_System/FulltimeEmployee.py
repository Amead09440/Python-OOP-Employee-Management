from Employee_System.Employee import Employee

class FullTimeEmployee (Employee) :
  def __init__ (self, Employee_id , Name , Hire_date , Base_Salary , Bonus_rate) : 
    super().__init__(Employee_id, Name, Hire_date, Base_Salary)
    self._Bonus_rate = Bonus_rate 
  
  # Calculate salary for full-time employees
  def Calculate_Salary (self) -> float:
    return self._Base_Salary + self._Bonus_rate
