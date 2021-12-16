"""
Implements the specialized (derived) class for a contract job vacancy
"""
import jobVacancy

class ContractJobVacancy(jobVacancy.JobVacancy):
    def __init__(self, jobCode, position, mininumQualifications, salaryOffered,contractDuration):
        super().__init__(jobCode, position, mininumQualifications, salaryOffered)
        if 0<= int(contractDuration) <= 12:
            self._contractDuration = int(contractDuration)
        else:
            raise ValueError("The month must to between 1-12")

    #override __str__ method by call base class __str__
    def __str__(self):
        return f"{super().__str__()},{self._contractDuration}"

    #override the parse method
    @staticmethod
    def parse(dataString):
        #separete string that contain data to parameter to create object
        fields = dataString.split(',')
        jobCode = fields[0]
        position = fields[1]
        mininumQualifications = fields[2]
        salaryOffered = fields[3]
        contraDuration = fields[4]
        
        # return a object created using the CSV
        return ContractJobVacancy(jobCode,position,mininumQualifications,salaryOffered,contraDuration)

    # Update the class definition as per the instructions in the PDF
    pass
