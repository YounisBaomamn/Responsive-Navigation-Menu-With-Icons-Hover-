emp={'emp_id':'','emp_name':'','emp_joining_date':'','emp_department':'','emp_salary':'','emp_age':''}
employee_lest=[]
def create():
    cr_rmp=int(input("How many empployees want to clean  number:  "))
    for i in range(cr_rmp):
        print ("\ncreate emploeey {}\n".format(i+1))
        new_emp=emp.copy()
        for key ,val in emp.items():
            new_empvaleu=input("Enter %s:  " %key )
            print('\n')
            new_emp[key]=pra_value(key,new_empvaleu)
            while key=='emp_id' and list(filter(lambda x: x[key]==new_emp[key],employee_lest)):
                print("Existed before id prepared id")
                new_emp[key]=int(input("Enter %s:  " %key ))
            
        employee_lest.append(new_emp)
    
def updat_dit():
    empp_id=int(input("\nEnter id emploeey  : "))
    upd_emp= list(filter(lambda x: x['emp_id']== empp_id, employee_lest))[0]
    for key ,val in upd_emp.aitems():
        if key == 'emp_id':continue
        nea_val=input("Enter {} new value \t".format(key))
        print('\n')
        upd_emp[key]=pra_value(key,nea_val)if nea_val else val

      
# def delet
def delete_employee():
   new_emp=int(input("Enter id employee :  " ))
   new_w=list(filter(lambda x: x['emp_id']==new_emp,employee_lest))[0]
   employee_lest.remove(new_w)

def searh():
    item=int(input('enter id or neam :  '))
    for i in range(len(employee_lest)):
     se_emp=(list(filter(lambda x: x['emp_id']==item,employee_lest))[i])
     print(se_emp)
     break
#pra_v    
def pra_value(key ,value):
    if key in ('emp_id','emp_salary')   :
        cor_valeu=int(value)
    else:
        cor_valeu=value
    return cor_valeu
        
def printt():
        print('\t1. EPrint th record of all employees')
        print('\t2. print employee register')
        num=int(input('Enter number: '))
        print('\n')
        if num==1:
            print('\temp_id  emp_name  emp_joining_date  emp_department  emp_salary \n')
            for i in range(len(employee_lest)):
               pr_emp=employee_lest[i]
               for key,val in pr_emp.items():
                  print('\t ', pr_emp[key], end= "   ")
    
               print("\n")
        else:
            item=int(input('Enter id employes:  '))
            print('\n')
            for i in range(len(employee_lest)):
               print('\temp_id  emp_name  emp_joining_date  emp_department  emp_salary \n')
               se_emp=(list(filter(lambda x: x['emp_id']==item,employee_lest))[i])
               for key, val in se_emp.items():
                  print('\t ', se_emp[key], end= "   ")
               break
        
def main():
    poss=True
    while poss:
        unm=int(input('Enter an option to checkout: '))
        print('\n')
        if unm==1:
            create()
        elif unm==2:
            updat_dit()
           
        elif unm==7:
            delete_employee()
           
        elif unm==4:
           searh()
        elif unm==5:
            printt()
        elif unm==6:
         break
    
main()
