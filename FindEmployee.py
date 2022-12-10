# Google Problem (Simple) : 
# Write a class which helps do the folloing things
# 1. Assign a manager for an employee
# 2. Find if two employees share the same manager
# 3. Find if an manager is in the management chain of an employee

class FindEmployee:

    def __init__(self) -> None:
        self.EmpManagerDict:dict = {}
        pass

    def AssignManager(self,employee, manager)->None:
        self.EmpManagerDict[employee] = manager

    def ShareSameManager(self, employee1, employee2)->bool:
        if employee1 not in self.EmpManagerDict or employee2 not in self.EmpManagerDict:
            return False
        
        if self.EmpManagerDict[employee1] == self.EmpManagerDict[employee2]:
            return True

        return False

    def InManagementChainOfEmployee(self, mgr, emp):

        if emp not in self.EmpManagerDict :
            return False

        if self.EmpManagerDict[emp] == mgr:
            return True

        return self.InManagementChainOfEmployee(mgr,self.EmpManagerDict[emp])


        
def main():
    findEmp = FindEmployee()

    findEmp.AssignManager("a","m")
    findEmp.AssignManager("b","m")
    findEmp.AssignManager("m","d")
    findEmp.AssignManager("c","d")

    print("Do a and b share same manager? : " + str(findEmp.ShareSameManager("a","b")))
    print("Is d in management chain of a ? : " + str(findEmp.InManagementChainOfEmployee("d","a")))
    print("Is c in management chain of a ? : " + str(findEmp.InManagementChainOfEmployee("c","a")))
    print("Is d in management chain of c ? : " + str(findEmp.InManagementChainOfEmployee("d","c")))

main()