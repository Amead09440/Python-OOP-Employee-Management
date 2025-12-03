from abc import ABC, abstractmethod

# Create an abstract class for Employee
class Employee (ABC):
  def __init__ (self, Employee_id , Name ,  Hire_date , Base_Salary) : 
    self._Employee_id = Employee_id
    self._Name = Name
    self._Hire_date = Hire_date
    self._Base_Salary = Base_Salary
  # Get the employee details
  @property
  def Employee_Details ( self) -> str : 
    return f"Employee ID : {self._Employee_id} \nName : {self._Name} \nHire Date : {self._Hire_date} \nBase Salary : {self._Base_Salary}"
  # Abstract method to calculate salary
  @abstractmethod
  def Calculate_Salary (self) -> float:
    pass
  #  method to get full name
  def Employee_FullName (self) -> str : 
    return f"{self._Name} ({self._Employee_id})"