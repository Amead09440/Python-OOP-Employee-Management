from Employee_System.Employee import Employee


class PartTimeEmployee (Employee) :
  def __init__ (self, Employee_id , Name , Hire_date , Base_Salary , Hourly_rate, Hours_worked) : 
    super().__init__(Employee_id, Name, Hire_date, Base_Salary)
    self.Hourly_rate = Hourly_rate
    self.Hours_worked = Hours_worked
  
  # Calculate salary for part-time employees
  def Calculate_Salary (self) -> float:
    # Salary is calculated as base salary plus hourly rate multiplied by hours worked
    return self._Base_Salary + (self.Hourly_rate * self.Hours_worked)