#Machine Problem 7
#Mehul Antony
#Prof. Mike Liljegren

#Description:This program reads data from a text file "1300-MP6 Data.txt" which
#contains information about students who have taken an unknown number of exams.
#We create a Student class with instance variables, public instance methods,
#and a private instance method. We then define two functions updateName and
#updateTest, which prompts the user to enter the first and last names of a
#student, and also prompts the user to enter test scores for a student respectively.



class Student:
    def __init__(self, stuID, name=None, testScores=None, avg=0.0):
        self._stuID = stuID
        if name is None:
            self._name = ["", ""]
        else:
            self._name = name
        if testScores is None:
            self._testScores = []
        else:
            self._testScores = testScores
        self._avg = avg

    def __str__(self):
        return f"Student: {self._stuID} {' '.join(self._name)}\nTest Scores: {' '.join(map(str, self._testScores))}\nTest Average: {self._avg:.2f}"

#Public instance methods
        
    def getID(self):
        return self._stuID

    def getName(self):
        return self._name

    def getTestScores(self):
        return self._testScores

    def getAvg(self):
        return self._avg

    def setName(self, firstName, lastName):
        self._name = [firstName, lastName]

    def addTest(self, testScore):
        self._testScores.append(testScore)
        self.__calcAvg()

#Private instance method
        
    def __calcAvg(self):
        if self._testScores:
            self._avg = sum(self._testScores)/len(self._testScores)
        else:
            self._avg = 0.0
        return self._avg

def getStudents():

# Opens the data file of student info... studentID, firstName, lastName, then
# testScores - the number of test scores is variable, from zero up... reads
# each line of data as a str, divides the line into the values... str, str, str,
# int, int, int... (a variable number of int values - could be none)...
# instantiates a new Student object, uses the Student object's instance methods
# to add those values to the object, adds the Student object to a dictionary of
# Student objects using studentID as the key and the Student object as the value,
# and returns the dictionary of Student objects.
#
# There are no parameters.
#
# Returns a dict of objects from the Student class, using student ID as the key
# and the Student object as the value

    students_dict = {}
    with open(r"C:\Users\anton\Downloads\1300 - MP6 Data.txt") as myFile:
        
        for line in myFile:
            elements = line.strip().split()
            student_id = elements[0]
            first_name = elements[1]
            last_name = elements[2]
            scores = [int(score) for score in elements[3:]]

            student = Student(student_id)
            student.setName(first_name, last_name)
            for score in scores:
                student.addTest(score)

            students_dict[student_id] = student
            
    return students_dict

def printStudents(roster):
    
# Prints the information for each Student object in roster... including studentID,
# firstName, lastName, testScores, and average for each object.
#
# roster A dict of objects from the Student class, each object contains a
# studentID(str), firstName(str), lastName(str),
# testScores(list of int value), and average (float).
#
# There is no return value.

    print("Students in roster:")
    for key, value in roster.items():
        
        print("Name:", key," ".join(value.getName()))
        test_scores = value.getTestScores()
        if test_scores:
            print("Test Scores:", " ".join(map(str,test_scores)))
        else:
            print("Test Scores: ")
        print("Test Average: {:.2f}".format(value.getAvg()))
        print()
        

def updateName(roster, stuID):

# Prompts the user to enter the first name and last name of a student. Then,
# uses the setName() instance method to change the name for the Student object
# in the dictionary roster with the key = stuID.
#
# roster A dictionary of objects from the Student class, using stuID as the
# key, and a Student object as the value.
# stuID A str that is the key for a Student object in the dictionary roster.
#
# There is no return value.

    print("You may update any student info, or add a student.")

    new_stuID = input("Enter Student ID(<enter> to stop): ")

    if new_stuID not in roster:
        print("This student does not exist. You may enter the info now.")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        roster[new_stuID] = Student(new_stuID)
        roster[new_stuID].setName(first_name, last_name)

        
        print("New Student Added:")
        print(f"Student: {new_stuID} {first_name} {last_name}")

        test_scores = roster[new_stuID].getTestScores()
        if test_scores:
            print("Test Scores:", " ".join(map(str, test_scores)))
        else:
            print("Test Scores: ")
        print("Test Average: {:.2f}".format(roster[new_stuID].getAvg()))

def updateTests(roster, stuID):

# Prompts the user to enter test scores for a student using addTest() to add
# each one to the Student object in the dictionary roster with the key = stuID.
#
# roster A dictionary of objects from the Student class, using stuID as the
# key, and a Student object as the value.
# stuID A str that is the key for a Student object in the dictionary roster.
#
# There is no return value.

    continue_input = True
    while continue_input:
        if stuID not in roster:
            print("This student does not exist. You may enter the info now.")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            roster[stuID] = Student(stuID)
            roster[stuID].setName(first_name, last_name)

        test_scores = []
        input_complete = False
        while not input_complete:
            test_score_input = input("Enter a Test Score (<enter> to stop): ")
            if test_score_input:
                test_score = int(test_score_input)
                roster[stuID].addTest(test_score)
                test_scores.append(test_score)
            else:
                input_complete = True

        print(f"New Student Added:\nStudent: {stuID} {' '.join(roster[stuID].getName())}")
        if test_scores:
            print("Test Scores:", " ".join(map(str, test_scores)))
        else:
            print("Test Scores: ")
        print("Test Average: {:.2f}".format(roster[stuID].getAvg()))

        continue_options = False
        while not continue_options:
            print("(1) Change the Name")
            print("(2) Add a Test")
            print("(3) Do Nothing")

            choice = input("What would you like to do? ")
            if choice == "1":
                new_first_name = input("First Name: ")
                new_last_name = input("Last Name: ")
                roster[stuID].setName(new_first_name, new_last_name)
                print(f"Student: {stuID} {new_first_name} {new_last_name}")
            elif choice == "2":
                test_score = int(input("Enter a Test Score (<enter> to stop): "))
                while test_score:
                    roster[stuID].addTest(test_score)
                    test_score = input("Enter a Test Score (<enter> to stop): ")
            elif choice == "3":
                continue_options = False
                continue_input = False


roster = getStudents()

printStudents(roster)
updateName(roster, "")
updateTests(roster, "")


