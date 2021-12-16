"""
Implements the general (base) class for a job vacancy
"""


class JobVacancy:
    def __init__(self, jobCode, position, mininumQualifications, salaryOffered):
        self._jobCode = jobCode
        self._position = position
        self._mininumQualifications = mininumQualifications
        self._salaryOffered = salaryOffered

    # Update the class definition as per the instructions in the PDF
