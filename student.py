                            ####       BUSINESS LOGIC LAYER     ####
class Student:

    s_list=[]
    userlist=[]
    passlist=[]

    def __init__(self):
        self.id=0
        self.age=0
        self.name=""
        self.year=0
        self.branch=""
        self.semester=""
        self.prev_score=0

## function to add student

    def add_student(self):
        Student.s_list.append(self)

  ##function to search a student

    def search_student(self,prev_score):
        for e in Student.s_list:
            if prev_score==e.prev_score:
                return e
        return False
        
    def new_student(self,nusername,npassword):
        if nusername not in Student.userlist:
            if (len(nusername)<=10):
                if (len(npassword)>=6):
                    Student.userlist.append(nusername)
                    Student.passlist.append(npassword)
                    return 1
                else:
                    return 2
            else:
                return 3
        else:
            return 4

    def login_student(self,ousername,opassword):
        if ousername in Student.userlist:
            if opassword in Student.passlist:
                if (len(opassword)>6):
                     if Student.userlist.index(ousername)==Student.passlist.index(opassword):
                          return True
                     else:
                         return 1
            else:
                return 2
        else:
            return 3

 

                      ####            PRESENTATION LAYER             ####
print()
print("################    WELCOME TO ABC SERVICES PVT LTD      ##################")
print()
print("PRESS KEY 1 IF YOU ARE NEW AND WANT TO SIGN UP")
print("PRESS KEY 2 IF YOU ARE AN EXISTING USER")
print()
ch=int(input("Enter your choice- \n "))

if (ch==1):
    while(1):
       new=Student()
       nusername=input("Enter new user name you want to create like (  john123  )\n ")
       npassword=input("Enter a strong password\n ")
       print()
       k=new.new_student(nusername,npassword)
       if (k==1):
           print("Username and password Updated Succesfully")
           print()
           break
       elif (k==2):
          print("Length of password should be more than 6 digits ")
          continue
       elif (k == 3):
           print("Lenth of username should be less than 10 digits ")
           continue
       elif (k==4):
           print("Username is already taken ")
           continue

while(1):
    print("Enter your credentials to login- ")
    log=Student()
    ousername=input("Enter your Username- ")
    opassword=input("Enter your Password- ")
    k=log.login_student(ousername,opassword)
    if (k==True):
         print("################## -WELCOME- ####################")
         print()
         break
    elif (k==1):
        print("Length of the password should be more than 6 ")
        continue
    elif (k==2):
        print("Username and password do not match")
        continue
    elif (k==3):
        print("You are not a registered user")
        break
while (1):
    print("Press 1 to Add new student")
    print("Press 2 to display all customer")
    print("Press 3 to search using previous sem score")
    print("Press 4 to Exit")
    print()
    c = int(input("Enter your choice:- "))
    if (c==1):
        st=Student()

        while(1):
            st.id = input("Enter the student id- ")
            if (len(st.id) == 3 and st.id.isnumeric()):
                break
            else:
                print ("eneter a valid 3 digit number")
                continue
        while(1):
            st.age=input("Enter the age of the student- ")
            if (st.age <= 25 and st.age.isdigit()):
                break
            else:
                print("Student age should be less than 25 years ")
                continue
        while(1):
            st.name = input("Eneter the name of the st- ")
            if (st.name.isalpha() or st.name==" "):
                break
            else:
                print("Name cannot contain digits it should contain only alphabets and should be separated by a space ")

        while (1):
            st.year = input("Enter the year- ")
            if (len(st.year) == 1 and st.year.isdigit()):
                break
            else:
                print("year should be one digit long ")
        while (1):
            st.branch = input("Enter the branch- ")
            if (len(st.branch) == 4 ):
                break
            else:
                print("year should be 4 characters long ")
                continue
        while (1):
            st.semester = input("Enter the sem- ")
            if (len(st.semester) == 1 and st.year.isdigit()):
                break
            else:
                print("sem should be one digit long ")
                continue
        while (1):
            st.prev_score = input("Enter the prev_score- ")
            if (st.prev_score.isdigit()):
                break
            else:
                print("digit long ")
                continue
            ## function call to add Student information
        st.add_student()
        print("Student Added Succesfully")
        
    elif (c==2):
        for e in Student.s_list:
            print("id=",e.id)
            print('name=',e.name)
            print('age=',e.age)
            print('branch=',e.branch)
            print('year=',e.year)
            print('semester=',e.semester)
            print('prev_score=',e.prev_score)
        #print(Student.s_list)
        # for e in Student.s_list:
        #     print("id=",e.id)
        #     print('name=',e.name)
        #     print('age=',e.age)
        #     print('branch=',e.branch)
        #     print('semester=',e.semester)
        #     print('year=',e.year)
        #     print('prev_score=',e.prev_score)
    
    elif (c==3):
        prev_score=input("Enter the score of the student you want to search:...")
        y=Student()
        m=y.search_student(prev_score)
        if (m==False):
            print()
            print("ERROR:-  (Respective Student Does Not Exist)")
            print()
        else:
            print()
            print("Student id:     ",m.id)
            print("Student age:    ",m.age)
            print("Student name:   ",m.name)
            print("Student year: ",m.year)
            print("Student branch: ",m.branch)
            print("Student semester: ",m.semester)
            print("Student prev_score: ",m.prev_score)
            print()
    elif (c==4):
        print("                  THANK YOU FOR USING ABC SERVICES                ")
        break
        exit(0)











