
count = 0

while count<3:
    budget =  input("whats your budget?")

    budget = int(budget)
    
    if budget==0:
        print("invalid amount: " + str(budget))
        continue

    elif budget < 0:
        print("No negative values allowed")
        break
    
    elif budget < 100:
        print("Minumum budget should be 100")
        continue   
    
    else:
        print("All good, let's proceed with the booking")
        break
    
    count += 1
    
print ("Process completed")


    
    


