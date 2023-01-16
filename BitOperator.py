def show_result():
    while True:
        operation = input("'1' to see the enabled bits or '2' to convert bits to integer or 'q' to quit: ") #ask user which operation they want to perform
        if operation == 'q':
            break
        elif operation == '1':
            num = input("Enter a 32-bit integer: ") #display bits of a 32bit integer by 
            try:
                num = int(num)
                for i in range(31, -1, -1): #iterate through the bits
                    if num & (1 << i): #bit shifting, check if the corresponding bit is 1
                        print(i, end=" ") #print the bits
                print()
            except ValueError:
                print("Invalid input, please enter a valid 32-bit integer.")
        elif operation == '2':
            bits = input("Enter the bit positions seperated by ' ': ")
            try:
                bits = [int(b) for b in bits.split(' ')] #form a list of the input bits
                if all(map(lambda x: 0 <= x <= 31, bits)): #check if bits are in the 32bit integer range
                    result = 0 #initial value
                    for bit in bits:
                        result |= (1 << bit) #iterate through the list of bit positions
                    print(result) #print the 32bit integer
                else:
                    print("Invalid input, please only enter valid bit positions (0-31).")
            except ValueError:
                print("Invalid input, please only enter valid bit positions (0-31).")
        else:
            print("Invalid option, please enter '1', '2' or 'q'.")

show_result()