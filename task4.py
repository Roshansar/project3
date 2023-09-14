Name=input("enter your name:")
registerno=int(input("enter your register no:"))
course=input("course:")
mark1=int(input("enter mark1 :"))
mark2=int(input("enter mark2 :"))
mark3=int(input("enter mark3:"))
mark4=int(input("enter mark4:"))
mark5=int(input("enter mark5:"))
mark6=int(input("enter mark6:"))
sum=mark1+mark2+mark3+mark4+mark5+mark6;
average=sum/6;
max_value=100;
if(mark1 > 40 and mark2 >40 and mark3> 40 and mark4> 40 and mark5> 40 and mark6> 40):
 print("congratulation you have passed..!")
else:
  print("OOPS!! Failed")
if(mark1>80 and mark2>80 and mark3>80 and mark4>80 and mark5>80 and mark6>80):
  print("Grade A...")
elif(mark1>=70 and mark2>=70 and mark3>=70 and mark4>=70 and mark5>=70 and mark6>80):
  print("Grade B..")
elif(mark1>=60 and mark2>=60 and mark3>=60 and mark4>=60 and mark5>=60 and mark6>=60):
  print("Grade C..")
elif(mark1>=50 and mark2>=50 and mark3>=50 and mark4>=50 and mark5>=50 and mark6>=50):
  print("Grade D..")
elif(mark1<=40 and mark2<=40 and mark3>=40 and mark4>=40 and mark5>=40 and mark6>=40):
  print("Grade E..")
else:
  print("keep trying..!!")
print(average)
