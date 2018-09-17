class Student:
    user_details=[]
    def  __init__(self):
        self.name=''
        self.age=0
        self.branch=''
        self.year=0
        self.semester=0
        self.prev_score=0
       
        user_detail=[]
       
   
    def add_user(self):
        name=input("enter name ")
        age=input("enter age ")
        branch=input("enter branch")
        year=input("enter year ")
        semester=int(input("enter sem "))
        prev_score=input("enter score ")
        dict_of_user={'name': name,'age':age,'branch':branch,'year':year,'semester':semester,'prev_score':prev_score}
        Student.user_details.append(dict_of_user);
   
    def show_user(self):
        print(self.user_details)
    def search(self,prev_ser):
        for e in Student.user_details:
            if(e.prev_score==prev_ser):
                print(e.name,e.age,e.branch,e.prev_score,e.year)
while(1):
    st= Student();
    print("\t\t\tWELCOME TO STUDENT MANAGEMENT SYSTEM")
    cont='y'
    while(cont=='y'):
        st.add_user()
        print("printing user detials")
        st.show_user()
        prev_ser=input('enter the score of student to be searched')
        st.search(prev_ser)
   
    cont=input("enter y to continue else n")
