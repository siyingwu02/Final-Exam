"""
Implements interaction with the end user and drives the application logic
"""
import jobVacancy
import contractJobVacancy


class JobVacancyApp:
    

    def run(self):
        try:
            InstanceOfBothClass = {} # use to hold the instance of class JobVacancy and class ContraJobVacaans
            # open the file in read mode
            with open("job.csv", "r") as fileRef:
                for line in fileRef:
                    jobVacancyObj = jobVacancy.JobVacancy.parse(line.strip())
                    contractJobVacancyObj = contractJobVacancy.ContractJobVacancy.parse(line.strip())
                    # store data into dictionay
                    InstanceOfBothClass[jobVacancyObj.getJobCode()] = jobVacancyObj
                    InstanceOfBothClass[contractJobVacancyObj.getJobCode()] = contractJobVacancyObj
                    
        
            def addJobVacancy(self,jobCode, position, mininumQualifications, salaryOffered):
                jobVacancy.JobVacancy(self,jobCode, position, mininumQualifications, salaryOffered)
                saveToFile(InstanceOfBothClass)

            def addContraJobVacancy(self,jobCode, position, mininumQualifications, salaryOffered,contractDuration):
                contractJobVacancy.ContractJobVacancy(self, jobCode, position, mininumQualifications, salaryOffered, contractDuration)
                saveToFile(InstanceOfBothClass)

            @staticmethod
            def saveToFile(InstanceOfBothClass):
                stringList = []

                for jobCode in InstanceOfBothClass:
                    objStrForm = str(InstanceOfBothClass[jobCode])
                    #add the string that contain all book data to the list
                    stringList.append(objStrForm+'\n')

                # open file in write mode
                with open("job.csv", 'w') as fileRef:
                # write the list of strings into the file
                    fileRef.writelines(stringList)

            """
            using a loop to show the options to the user until user select terminatate appilcation
            """
            selection = 0
            while selection != "d":
                print("Welcome to Job Vacancy App")
                selection = input("----------------Main Menue----------------\na. Add A Job Vancancy\nb. Add A Contract Job Vacancy\nc. Search Job Vancancy by Job Code\nd. Terminate Application")
                if selection.lower() == "a":
                    jobCode = input("Please Enter the Job Code: ")
                    position = input("Please Enter the Position: ")
                    mininumQualifications = input("Pleasse Enter the mininum qualifications: ")
                    salaryOffered = int(input("Please Enter the Salary Offered: "))
                    addJobVacancy(jobCode, position, mininumQualifications, salaryOffered)
                    print("Create new job vacancy successfully.")

                elif selection.lower() == "b":
                    jobCode = input("Please Enter the Job Code: ")
                    position = input("Please Enter the Position: ")
                    mininumQualifications = input("Pleasse Enter the mininum qualifications: ")
                    salaryOffered = int(input("Please Enter the Salary Offered: "))
                    contractDuration = int(input("Please Enter the Contract Duration"))
                    addContraJobVacancy(jobCode, position, mininumQualifications, salaryOffered,contractDuration)
                    print("Create new contract job vacancy successfully.")


                elif selection.lower() == "c":
                    jobCode = input("Please Enter the Job Code to search")
                    if jobCode in InstanceOfBothClass:
                        print(InstanceOfBothClass[jobCode])
                    else:
                        print("Job code not exist")

                else:
                    selection = input("selection not exist, please enter a,b,c,or d to select")
        except FileNotFoundError:
            pass

        except ValueError as err:
            print(f"The input is error{err.args}")

JobVacancyAppObj = JobVacancyApp.run()
