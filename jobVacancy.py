"""
Implements the general (base) class for a job vacancy
"""


from typing import Text


class JobVacancy:
    def __init__(self, jobCode, position, mininumQualifications, salaryOffered):
        self._jobCode = jobCode
        self._position = position
        self._mininumQualifications = self.setMininumQualifications(mininumQualifications)
        self._salaryOffered = salaryOffered

    #create accessor for the jobCode
    def getJobCode(self):
        return self._jobCode

    #define mutator of mininumQualifications
    def setMininumQualifications(self, newMininumQualifications):
        if newMininumQualifications.lower() == "diploma" or newMininumQualifications.lower() == "bachelors" or newMininumQualifications.lower() == "masters" or newMininumQualifications.lower() == "doctorate":
            self._mininumQualifications = newMininumQualifications
        else:
            raise ValueError ("The input mininum qualifications is not one of diploma, bachelors, masters, or doctorate")

    #override __str__ method of instance
    def __str__(self):
        return f"{self.getJobCode},{self._position},{self._mininumQualifications},{self._salaryOffered}"

    @staticmethod
    def parse(dataString):
        #separete string that contain data to parameter to create object
        fields = dataString.split(',')
        jobCode = fields[0]
        position = fields[1]
        mininumQualifications = fields[2]
        salaryOffered = fields[3]
        
        # return a object created using the CSV
        return JobVacancy(jobCode,position,mininumQualifications,salaryOffered)
   # Update the class definition as per the instructions in the PDF
