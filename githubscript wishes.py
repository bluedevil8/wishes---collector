#this script allows the user to enter personal wishes , sort them and remove any if desired 
#created by blue devil
#insta:Madev_87

print("welcome every body , here is were u can write ur own wishes , enjoy!!!!")
name1=input("enter ur name dear:_").lstrip().upper()
time=input(f"how many wishes u have? dear \n {name1} ").lstrip()
if time.isdigit():
    time1=int(time)
    list3=[]#list always should be not in loop
    for i in range(time1):
        wishes=input(f"enter ur wishes {i}")
        list3.append(wishes)
        print(list3)
        other_wishes=input("dou want to add a single last wish? if yes tape 1 , i not tape 0")
        try:
            v1=(other_wishes==1)#true
            v2=(other_wishes==0)#false
        except TypeError:#cause int we cant use it with str
            other_wishes=int(input("dou want to add a single last wish? if yes tape 1 , i not tape 0"))
            v1 = (other_wishes == 1)  # true
            v2 = (other_wishes == 0)  # false
            #like when u say its true
            if v1:
                value4=input("enter ur wish:")
            elif v2:
                list3.sort()
                print(list3)
                remove_i=int(input("do u want to remove any wish? if yes tap 1 , if no tap 0"))
                yes=(remove_i==1)#true
                no=(remove_i==0)#false
                remove_i1=str(remove_i)
                if yes :
                    list3.remove(remove_i1)
                elif no:
                    print(list3)
                    print("good bye guys!")





