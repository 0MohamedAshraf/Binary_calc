'''
Eslam Gabr Abd-Alazim        =>  20230058
Mohamed Ashraf Said Ibrahim  =>  20230320
Mohamed Ahmed Kotb           =>  20230315
'''
print("** binary calculator **")

def binary_subtraction(binary1, binary2):
    # Equate the number of bits of both binary numbers
    max_len = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(max_len)
    binary2 = binary2.zfill(max_len)
    res = []
    borrow = 0
    for bit1, bit2 in zip(reversed(binary1), reversed(binary2)):
            sub = int(bit1) - int(bit2) - borrow # diff between 2 bits
            if sub < 0 :
                sub += 2 # borrow 1 from the adjacent bit
                borrow = 1
            else:
                borrow = 0
            res.append(str(sub))

    res.reverse()
    return ''.join(res)




def binary_addition(binary1, binary2):
    max_len = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(max_len)
    binary2 = binary2.zfill(max_len)

    result = ''
    carry = 0

    for bit1, bit2 in zip(reversed(binary1), reversed(binary2)):
        bit_sum = int(bit1) + int(bit2) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2

    if carry:
        result = '1' + result

    return result

def ones_complement(number):
    complement_bits = ['1' if bit == '0' else '0' for bit in number]
    return ''.join(complement_bits)


def twos_complement(number):
    ones_complement_bits = ['1' if bit == '0' else '0' for bit in number]
    ones_complement = ''.join(ones_complement_bits)
    twos_complement = binary_addition(ones_complement, '1')

    return twos_complement


def check_numbers_binary(number):
    check = str(number)
    # Define the list of allowed digits
    allowed_digits = {'1', '0'}

    # Check if all digits in the user's input are in the allowed set
    if set(check).issubset(allowed_digits):
        return True

    else:
        print("please insert a valid binary number")


#menu_1
while True:
        print("A) Insert new numbers ")
        print("B) Exit Program ")

        choice = input("Please choose A/B ").upper()
        if choice == "A":
            while True:
                print("Please insert The first number ")
                num1 = input("First number: ")  # First number from the user
                if check_numbers_binary(num1):
                    break
                else:
                    print("please insert a valid binary number")

#menu_2
            while True:

                print("**Please select the operation**")
                print("A) Compute one's complement")
                print("B) Compute two's complement")
                print("C) addition")
                print("D) subtraction")

                choice_2 = input("").upper()
                if choice_2 == "A":
                    result1 = ones_complement(num1)
                    print("Original number = ", num1)
                    print("one's complement = ", result1)
                    break

                elif choice_2 == "B":
                    result1 = twos_complement(num1).zfill(len(num1))
                    print("Original number = ", num1)
                    print("two's complement = ", result1)
                    break
                elif choice_2 == 'C' or choice_2 == 'D':
                    while True:
                        num2 = input("Please insert the second number: ") # second number from the user
                        if check_numbers_binary(num2):
                            break
                        else:
                            print("Please insert a valid binary number.")

                    if choice_2 == "C":
                        print("First number = ", num1)
                        print("Second number = ", num2)
                        print("Their sum = ", binary_addition(num1,num2))
                        break
                    elif choice_2 == "D":
                        if len(num2) >len(num1):
                            print("error: can't subtract if second number > First number ") # Error
                            continue
                        print("First number = ", num1)
                        print("Second number = ", num2)
                        print("Their difference = ", binary_subtraction(num1, num2))
                        break
                else:
                    print("Please select a valid choice")
        elif choice == "B":
            print("Exiting Program ")
            break  # EXit the program
        else:
            print("Invalid choice")
            print("Please select a valid choice")
            continue



