def countDown(num: int):
    # Check if num is equal to or less than 0. Stops execution if equal or less than 0.
    if (num <= 0):
        print("Done!")
        return
    # Prints what was passed in as num 
    print(f"{num}")
    # Decrements num by 1 
    num -= 1
    # After decrementing num by 1 calls the function again and passes in the next number after previous one. 
    countDown(num)

countDown(10)
    