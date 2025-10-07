def number_pattern_generator(num):
    count = 1
    for i in range(1,(num*2)):
        print(count,end="\n")
        if i < num:
            count+=1
        else:
            count-=1
        for j in range(1,count):
            print(j,end="")

number  = int(input("Enter the number:"))

number_pattern_generator(number)
