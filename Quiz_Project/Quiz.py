import json

def Admin(dic):
    T=True
    while T:
        print("1. View Quizzes\n2. Create Quiz \n3. Edit Quiz\n4. Delete Quiz\n5. View Topics\n6. Logout")
        n=int(input("Choose what you want: "))
        if(n==1):
            show_quiz(dic)
            
        elif(n==2):
            Type=input("Subject: ")
            Level=input("Level: ")
            Question_no=input("Ques_Id: ")
            Ques=input("Question: ")
            Count=int(input("How many option: "))
            Option=list(input("option: ") for i in range(Count))
            Answer=input("Answer: ")
            
            dic["quiz"][Type]={Level:{Question_no:{"Question":Ques, "options": Option,"Answer":Answer}}}
            dump_data = json.dumps(dic)
            fp = open('database.json','w+')
            fp.write(dump_data)
            fp.close()
        
        elif(n==3):
            show_topics(dic)
            Subj=input("In which topic you want to edit: ")
            for Level in dic['quiz'][Subj]:
                print(Level)
                print('==============')
                Question_counter = 1
                for Question_no in dic['quiz'][Subj][Level]:
                    print(str(Question_counter)+')',dic['quiz'][Subj][Level][Question_no]['Question'])
                    Question_counter+=1
                    option_counter = 97
                    for option in dic['quiz'][Subj][Level][Question_no]['options']:
                        print(chr(option_counter)+'.',option)
                        option_counter+=1
            s=int(input("What you want to edit: \n1. Question \n2. Options\n3. Answer\n ---> " ))
            Level=input("In which Level (Easy, Medium, Hard):  ")
            Ques=input("which Question id (eg: q1, q2) : ")
            
            if(s==1):
                edit_quiz(dic,Subj,Level,Ques)
            elif(s==2):
                edit_options(dic,Subj,Level,Ques)
            elif(s==3):
                edit_Answers(dic,Subj,Level,Ques)
            
            dump_data = json.dumps(dic)
            fp = open('database.json','w+')
            fp.write(dump_data)
            fp.close()
        
        elif(n==4):
            quiz_data=dic["quiz"]
            c=1
            for Type in quiz_data:
                print(c,Type) 
                c+=1
            Subj=input("which Subject you want to delete: ")
            del dic["quiz"][Subj]
            print(Subj, "quiz is deleted")
            dump_data = json.dumps(dic)
            fp = open('database.json','w+')
            fp.write(dump_data)
            fp.close()
            
        elif(n==5):
            show_topics(dic)
                
        elif(n==6):
            return




def result(dic,di,Subj,Level,user):
    c=0
    print(user)
    for i in di:
   
        if(dic["quiz"][Subj][Level]['q'+str(i)]["Answer"]== dic["quiz"][Subj][Level]['q'+str(i)]["options"][di[i]]):
            c+=1
        print("Q{0}) Your Answer is {2}\n    Correct Answer is {1}".format(i,dic["quiz"][Subj][Level]['q'+str(i)]["Answer"],dic["quiz"][Subj][Level]['q'+str(i)]["options"][di[i]]))
    print("Total Percentage: {}%".format(round(c/len(di)*100),2))
    
    
    

def attempter(dic,user):
    
    while True:
        n=int(input("1. Take Quiz\n2. Logout \n"))
        if(n==1):
            t=show_topics(dic)
            c=int(input("Choose topic: "))
            Subj=t[c-1]
            k=["Easy", "Medium", "Hard"]
            print("1. Easy    2. Medium     3.Hard")
            l=int(input("Chosse Level: "))
            Level=k[l-1]
            di={}
            Question_counter = 1
            for Question_no in dic['quiz'][Subj][Level]:
                print(str(Question_counter)+')',dic['quiz'][Subj][Level][Question_no]['Question'])
                option_counter = 1
                for option in dic['quiz'][Subj][Level][Question_no]['options']:
                    print(str(option_counter) +'] ',option)
                    option_counter+=1
                ans=int(input("Answer: "))
                di[Question_counter]=ans
                Question_counter+=1
            result(dic,di,Subj,Level,user)
    
        elif(n==2):
            return
    
    
    
    
    
    
    
def Login(dic):
    
    while True:    
        print("Please Login: ")
        user=input("User Id : ")
        password=input("Password: ")
        if(user in dic["user"]):
            if(dic["user"][user]==password):
                if(user=="admin"):
                    print("Login Successful")
                    dump_data = json.dumps(dic)
                    fp = open('database.json','w+')
                    fp.write(dump_data)
                    fp.close()
                    Admin(dic)  
                else:
                    attempter(dic,user)
                break
        else:
            print("User does not exist,First Register please")
            dic=registeration(dic)      
    return dic


def registeration(dic):
    
    while True:
        user=input("User Id : ")
        password=input("Password: ")
        if(user in dic["user"]):
            print("Username is already exits, please choose another username ") 
            continue
        dic["user"][user]=password 
        print("Registration Successfull")
        dump_data = json.dumps(dic)
        fp = open('database.json','w+')
        fp.write(dump_data)
        fp.close()

        break
    return dic

def edit_quiz(dic,Subj,Level,Ques):
    print(dic["quiz"][Subj][Level][Ques]["Question"])
    Question=input("Edit Question: ")
    dic["quiz"][Subj][Level][Ques]["Question"]=Question
    return dic

def edit_options(dic,Subj,Level,Ques):
    counter=1
    for option in dic['quiz'][Subj][Level][Ques]['options']:
        print(counter,option)
        counter+=1
    a=int(input("Which option do you want to edit? "))
    dic['quiz'][Subj][Level][Ques]['options'][a-1]=input("Enter an Option: ")
    return dic
    
def edit_Answers(dic,Subj,Level,Ques):
    print(dic["quiz"][Subj][Level][Ques]["Answer"])
    Answer=input("Edit Answer: ")
    dic["quiz"][Subj][Level][Ques]["Answer"]=Answer
    return dic

def show_topics(dic):
    print("Topics are : ")
    quiz_data=dic["quiz"]
    counter=1
    li=[]
    for i in quiz_data:
        print(counter,"->",i) 
        counter+=1
        li.append(i)
    return li

def show_quiz(dic):
    quiz_data = dic['quiz']
    for Type in quiz_data:
        print(Type)
        print('-------')
        for Level in quiz_data[Type]:
            print(Level)
            print('--------')
            Question_counter = 1
            for Question_no in quiz_data[Type][Level]:
                print(str(Question_counter)+')',quiz_data[Type][Level][Question_no]['Question'])
                Question_counter+=1
                option_counter = 97
                for option in quiz_data[Type][Level][Question_no]['options']:
                    print(chr(option_counter)+'.',option)
                    option_counter+=1
                
                print("Answer:",quiz_data[Type][Level][Question_no]['Answer'])
            print('\n')
            



if __name__=="__main__":
    fp = open('database.json','r')
    content = fp.read()
    dic = json.loads(content)
    fp.close()
    
    inup=input("Login or Register: ")
    
    if(inup=="Login"):
        
        Login(dic)
        print("Logout")
        
    elif(inup=="Register"):
        registeration(dic)