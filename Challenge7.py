def primenumber_rangefinder(start,end):
    if start == 1:
        start+=1
    for num in range(start,end+1):
        for n in range(2,num):
            if num%n == 0:
                break
        else:
            print(num)

            
start_range = int(input("Enter start range:"))
end_range = int(input("Enter end range:"))
primenumber_rangefinder(start_range,end_range)