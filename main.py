in_number=int(input("please enter your number:   "))
factorial=1
if in_number<=0:
      print(in_number)
else: 
    for i in range(1,in_number+1):
        factorial*=i
    print(factorial)
