"""
Implements the specialized (derived) class for a contract job vacancy
"""
import jobVacancy

class ContractJobVacancy(jobVacancy.JobVacancy):
    def __init__(self, jobCode, position, mininumQualifications, salaryOffered):
        super().__init__(jobCode, position, mininumQualifications, salaryOffered)
        self._contractDuration = 12

    #override __str__ method by call base class __str__
    def __str__(self):
        return f"{super().__str__()},{self._contractDuration}"

    # Update the class definition as per the instructions in the PDF
    pass
