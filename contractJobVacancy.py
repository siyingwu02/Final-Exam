"""
Implements the specialized (derived) class for a contract job vacancy
"""
import jobVacancy

class ContractJobVacancy(jobVacancy.JobVacancy):
    def __init__(self, jobCode, position, mininumQualifications, salaryOffered):
        super().__init__(jobCode, position, mininumQualifications, salaryOffered)
    # Update the class definition as per the instructions in the PDF
    pass
