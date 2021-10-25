import json

def edit_quiz(di,sub,level,ques):
    print(di["quiz"][sub][level][ques]["question"])
    question=input("Edit question: ")
    di["quiz"][sub][level][ques]["question"]=question
    return di

def edit_options(di,sub,level,ques):
    c=1
    for option in di['quiz'][sub][level][ques]['options']:
        print(c,option)
        c+=1
    b=int(input("Which option wants to edit: "))
    di['quiz'][sub][level][ques]['options'][b-1]=input("Enter option: ")
    return di
    
def edit_answers(di,sub,level,ques):
    print(di["quiz"][sub][level][ques]["answer"])
    answer=input("Edit answer: ")
    di["quiz"][sub][level][ques]["answer"]=answer
    return di

def show_topics(di):
    print("Topics are : ")
    quiz_data=di["quiz"]
    c=1
    l=[]
    for type_of_sub in quiz_data:
        print("{} -> {}".format(c,type_of_sub) )
        c+=1
        l.append(type_of_sub)
    return l

def show_quiz(di):
    quiz_data = di['quiz']
    for type_of_sub in quiz_data:
        print(type_of_sub)
        print('==============')
        for level in quiz_data[type_of_sub]:
            print(level)
            print('==============')
            question_counter = 1
            for question_no in quiz_data[type_of_sub][level]:
                print(str(question_counter)+')',quiz_data[type_of_sub][level][question_no]['question'])
                question_counter+=1
                option_counter = 97
                for option in quiz_data[type_of_sub][level][question_no]['options']:
                    print(chr(option_counter)+'.',option)
                    option_counter+=1
                
                print("Answer:",quiz_data[type_of_sub][level][question_no]['answer'])
            print('\n')
            

def Admin(di):
    T=True
    while T:
        print("1. View Quizzes\n2. Create Quiz \n3. Edit Quiz\n4. Delete Quiz\n5. View Topics\n6. Logout")
        n=int(input("Choose what you want: "))
        if(n==1):
            show_quiz(di)
            
        elif(n==2):
            type_of_sub=input("Subject: ")
            level=input("Level: ")
            question_no=input("Ques_Id: ")
            ques=input("question: ")
            count=int(input("How many option: "))
            option=list(input("option: ") for i in range(count))
            answer=input("answer: ")
            
            di["quiz"][type_of_sub]={level:{question_no:{"question":ques, "options": option,"answer":answer}}}
            dump_data = json.dumps(di)
            fp = open('database.json','w+')
            fp.write(dump_data)
            fp.close()
        
        elif(n==3):
            show_topics(di)
            sub=input("In which topic you want to edit: ")
            for level in di['quiz'][sub]:
                print(level)
                print('==============')
                question_counter = 1
                for question_no in di['quiz'][sub][level]:
                    print(str(question_counter)+')',di['quiz'][sub][level][question_no]['question'])
                    question_counter+=1
                    option_counter = 97
                    for option in di['quiz'][sub][level][question_no]['options']:
                        print(chr(option_counter)+'.',option)
                        option_counter+=1
            s=int(input("What you want to edit: \n1. Question \n2. Options\n3. Answer\n ---> " ))
            level=input("In which level (Easy, Medium, Hard):  ")
            ques=input("which question id (eg: q1, q2) : ")
            
            if(s==1):
                edit_quiz(di,sub,level,ques)
            elif(s==2):
                edit_options(di,sub,level,ques)
            elif(s==3):
                edit_answers(di,sub,level,ques)
            
            dump_data = json.dumps(di)
            fp = open('database.json','w+')
            fp.write(dump_data)
            fp.close()
        
        elif(n==4):
            quiz_data=di["quiz"]
            c=1
            for type_of_sub in quiz_data:
                print(c,type_of_sub) 
                c+=1
            sub=input("which subject you want to delete: ")
            del di["quiz"][sub]
            print(sub, "quiz is deleted")
            dump_data = json.dumps(di)
            fp = open('database.json','w+')
            fp.write(dump_data)
            fp.close()
            
        elif(n==5):
            show_topics(di)
                
        elif(n==6):
            return




def result(di,d,sub,level,user):
    c=0
    print(user)
    for i in d:
        #print(di["quiz"][sub][level]['q'+str(i)]["answer"],di["quiz"][sub][level]['q'+str(i)]["options"][d[i]])
        if(di["quiz"][sub][level]['q'+str(i)]["answer"]== di["quiz"][sub][level]['q'+str(i)]["options"][d[i]]):
            c+=1
        print("Q{0}) Your answer is {2}\n    Correct Answer is {1}".format(i,di["quiz"][sub][level]['q'+str(i)]["answer"],di["quiz"][sub][level]['q'+str(i)]["options"][d[i]]))
    print("Total percentage: {}%".format(round(c/len(d)*100),2))
    
    
    

def test_taker(di,user):
    
    while True:
        n=int(input("1. Take Quiz\n2. Logout\n choose: "))
        if(n==1):
            t=show_topics(di)
            s=int(input("Choose topic: "))
            sub=t[s-1]
            k=["Easy", "Medium", "Hard"]
            print("1. Easy    2. Medium     3.Hard")
            l=int(input("Chosse level: "))
            level=k[l-1]
            d={}
            question_counter = 1
            for question_no in di['quiz'][sub][level]:
                print(str(question_counter)+')',di['quiz'][sub][level][question_no]['question'])
                option_counter = 1
                for option in di['quiz'][sub][level][question_no]['options']:
                    print(str(option_counter) +'] ',option)
                    option_counter+=1
                ans=int(input("Answer: "))
                d[question_counter]=ans
                question_counter+=1
            result(di,d,sub,level,user)
    
        elif(n==2):
            return
    
    
    
    
    
    
    
def Login(di):
    
    while True:    
        print("Please Login: ")
        user=input("user_id : ")
        passw=input("password: ")
        if(user in di["user"]):
            if(di["user"][user]==passw):
                if(user=="admin"):
                    print("Login Succesful")
                    dump_data = json.dumps(di)
                    fp = open('database.json','w+')
                    fp.write(dump_data)
                    fp.close()
                    Admin(di)  
                else:
                    test_taker(di,user)
                break
        else:
            print("user does not exit Register please")
            di=registeration(di)      
    return di


def registeration(di):
    
    while True:
        user=input("user_id : ")
        passw=input("password: ")
        if(user in di["user"]):
            print("Username is exits, please choose other ") 
            continue
        di["user"][user]=passw 
        print("Registration Successfull")
        dump_data = json.dumps(di)
        fp = open('database.json','w+')
        fp.write(dump_data)
        fp.close()

        break
    return di

if __name__=="__main__":
    fp = open('database.json','r')
    content = fp.read()
    di = json.loads(content)
    fp.close()
    
    inu=input("Login or register: ")
    
    if(inu=="Login"):
        
        Login(di)
        print("Logout!!!")
        
    elif(inu=="register"):
        registeration(di)