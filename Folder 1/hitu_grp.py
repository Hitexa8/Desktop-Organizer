import numpy as np
import matplotlib.pyplot as plt 
import psycopg2

def connection():
    conn=psycopg2.connect(host="localhost",port="80",user="root",password="",database="Sem 3")
    cur=conn.cursor()
    return conn,cur

def details_of_students():
    number=int(input("\nHow many name you want to enter? "))
    d={}
    for i in range(number):
        names=input("Enter the name of student:")
        conn,cur=connection()
        names=names.upper()
        cur.execute(f"SELECT python,fsd,ps,de FROM student_data where Column8='{names}';")
        data=cur.fetchall()
        marks=[data[0][0],data[0][1],data[0][2],data[0][3]]
        d[names]=marks
    bar_graph(d)

def bar_graph(d): 
    x=["PYTHON","FSD","PS","DE"]
    index = np.arange(len(x))
    bar_width = 0.15

    for i,name in enumerate(d.keys()):
        plt.bar(index + i * bar_width, d[name], bar_width, label=name)
    
    for i, name in enumerate(d.keys()):
        for j, value in enumerate(d[name]):
            plt.text(index[j] + i * bar_width, value + 1, str(value), ha='center', va='bottom')

    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title('Scores by Student and Subject')
    plt.xticks(index + 1.5 * bar_width, x)
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.show()

def bar_graph_stu(d):
    x=["PYTHON"]
    index = np.arange(len(x))
    bar_width = 0.15
    for i,name in enumerate(d.keys()):
        plt.bar(index + i * bar_width, d[name], bar_width, label=name)
    
    for i, name in enumerate(d.keys()):
        for j, value in enumerate(d[name]):
            plt.text(index[j] + i * bar_width, value + 1, str(value), ha='center', va='bottom')

    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title('Scores by Student and Subject')
    plt.xticks(index + 1.5 * bar_width, x)
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.show()

def valid_num_of_stu(num):
    if num<=0:
        return False 
    return True

def check_branch(branch):
    conn,cur=connection()
    cur.execute(f"SELECT branch from student_data")
    data=cur.fetchall()
    conn.close()
    for i in data:
        if branch in i:
            return True
    else:
        return False

def top_branch(name,num):
    conn,cur=connection()
    num=str(num)
    cur.execute(f"SELECT python,fsd,ps,de,student_name from student_data where branch='{name}' LIMIT '{num}'")
    data=cur.fetchall()
    conn.commit()
    conn.close()
    d={}
    for i in data:
        marks=[i[0],i[1],i[2],i[3]]
        d[i[4]]=marks
    bar_graph(d)
 
def select_branch():
    print("1.CE.\n2.CSE\n3.IT\n4.Other\n5.Exit")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        num_stu=select_student()
        if not valid_num_of_stu(num_stu):
            print("Enter Valid Number of Students")
            return
        top_branch("CE",num_stu)
        return
    elif choice==2:
        num_stu=select_student()
        if not valid_num_of_stu(num_stu):
            print("Enter Valid Number of Students")
            return
        top_branch("CSE",num_stu)
    elif choice==3:
        num_stu=select_student()
        if not valid_num_of_stu(num_stu):
            print("Enter Valid Number of Students")
            return
        top_branch("IT",num_stu)
    elif choice==4:
        choice=int(input("Enter Branch of your Choice:"))
        if check_branch(choice.upper()):
            num_stu=select_student()       
            if not valid_num_of_stu(num_stu):
                print("Enter Valid Number of Students")
                return
            top_branch(choice,num_stu)
        else:
            print("Enter Valid Type of Branch")
    elif choice==5:
        print("Exited")
    else:
        print("Enter The Valid Choice")
        select_branch()

def top_depart(name,num):
    conn,cur=connection()
    num=str(num)
    cur.execute(f"SELECT python,fsd,ps,de,student_name from student_data where department='{name}' LIMIT '{num}'")
    data=cur.fetchall()
    conn.commit()
    conn.close()
    d={}
    for i in data:
        marks=[i[0],i[1],i[2],i[3]]
        d[i[4]]=marks
    bar_graph(d)

def select_depart():
    print("1.CE/IT-1.\n2.CE/IT-2\n3.CE/IT-3\n4.Exit")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        num_stu=select_student()
        if not valid_num_of_stu(num_stu):
            print("Enter Valid Number of Students")
            return
        top_depart("CE/IT-1",num_stu)
    elif choice==2:
        num_stu=select_student()
        if not valid_num_of_stu(num_stu):
            print("Enter Valid Number of Students")
            return
        top_depart("CE/IT-2",num_stu)
    elif choice==3:
        num_stu=select_student()
        if not valid_num_of_stu(num_stu):
            print("Enter Valid Number of Students")
            return
        top_depart("CE/IT-3",num_stu)
    elif choice==4:
        print("Exited")
        return
    else:
        print("Enter The Valid Choice")
        select_depart()

def select_student():
    print("1.5.\n2.10\n3.15\n4.Other\n5.Exit")
    choice=int(input("Enter Your Choice:"))    
    conn,cur=connection()
    if choice==1:
        return 5
    elif choice==2:
        return 10
    elif choice==3:
        return 5
    elif choice==4:
        choice=int(input("Enter Number of Students of your Choice:"))
        return choice
    elif choice==5:
        return 
    else:
        print("Enter The Valid Choice")
        select_student()

def top_subject(subject):
    num_stu=select_student()
    if not valid_num_of_stu(num_stu):
        print("Enter Valid Number of Students")
        return
    conn,cur=connection()
    num_stu=str(num_stu)
    data=""
    if subject=="python":
        cur.execute(f"SELECT python,student_name from student_data order by python desc LIMIT '{num_stu}'")
        data=cur.fetchall()
    elif subject=="Fsd":
        cur.execute(f"SELECT fsd,student_name from student_data order by fsd desc LIMIT '{num_stu}'")
        data=cur.fetchall()
    conn.commit()
    conn.close()
    d={}
    for i in data:
        marks=[i[0]]
        d[i[1]]=marks
    bar_graph_stu(d)

def search():
    print("1.Search within the Students.\n2.Top Students of Departments\n3.Top Students of Branch\n4.Top Students of Python\n5.Top Students of FSD\n6.Exit")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        details_of_students()
    elif choice==2:
        select_depart()
    elif choice==3:
        select_branch()
    elif choice==4:
        top_subject("python")
    elif choice==5:
        top_subject("Fsd")
    elif choice==6:
        return
    else:
        print("Enter The valid choice")

def Main():
    search()
Main()