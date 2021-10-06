def bin_add(bin_str_1, bin_str_2):
   length = len(bin_str_1) if len(bin_str_1) > len(bin_str_2) else len(bin_str_2)
   bin_str_1 = list(bin_str_1.zfill(length))
   bin_str_2 = list(bin_str_2.zfill(length))
   output = ''
   carry = 0
   for i in reversed(range(len(bin_str_1))):
      if carry == 0:
         if bin_str_1[i] == '0' and  bin_str_2[i] == '0':
            output = output + '0'
            carry = 0
         elif bin_str_1[i] == '1' and  bin_str_2[i] == '1':
            output += '0'
            carry = 1
         else:
            output += '1'
            carry = 0
      else:
         if bin_str_1[i] == '0' and  bin_str_2[i] == '0':
            output = output + '1'
            carry = 0
         elif bin_str_1[i] == '1' and  bin_str_2[i] == '1':
            output += '1'
            carry = 1
         else:
            output += '0'
            carry = 1
   if carry == 1:
      output += '1'
   print(output[::-1])
   return output[::-1]

def bin_subtract(bin1, bin2):
    length = len(bin1) if len(bin1) > len(bin2) else len(bin2)
    bin1 = list(bin1.zfill(length))
    bin2 = list(bin2.zfill(length))
    overflow = list('0' * length)
    answer = list('0' * length)

    for i in reversed(range(length)):
        result = int(bin1[i]) + int(overflow[i]) - int(bin2[i])

        if result == -1:
            if not i:
                return 'negative'

            searchindex = 1
            while not int(bin1[i - searchindex]):
                searchindex += 1
                if i - searchindex < 0:
                    return 'negative'

            for j in range(i - searchindex + 1, i + 1):
                overflow[j] = '1'

            overflow[i - searchindex] = '-1'
            answer[i] = '1'
        else:
            answer[i] = str(result)

    answer = ''.join(answer)
    return answer
    
def bin_multiply(bin1, bin2):
  to_sum = []

  for index, digit in enumerate(reversed(bin2)):
    row = ''
    for i in bin1:
      if int(digit) and int(i):
        row += '1'
      else:
        row += '0'
    row += '0' * index
    to_sum.append(row)

  output = to_sum[0]
  for i in range(1, len(to_sum)):
    output = bin_add(output, to_sum[i])
  return output

def bin_divide(bin1, bin2):
    bin1 = bin1[bin1.find('1'):]
    bin2 = bin2[bin2.find('1'):]
    if len(bin1) < len(bin2):
        return '0'

    segment = ''
    answer = ''

    for i in range(len(bin1)):
        segment += bin1[i]
        sub = bin_subtract(segment, bin2)

        if sub == 'negative':
            answer += '0'
        else:
            answer += '1'
            segment = sub
    return answer

def dec_to_bin(dec_num):
  binary_num = [128,64,32,16,8,4,2,1]
  binary = []
  bin_string = ''

  for num in binary_num:
    if dec_num >= num:
      dec_num -= num
      binary.append(1)
    else:
      binary.append(0)

  for bin_num in binary:
    bin_string += str(bin_num)

  return bin_string

# Binary to Decimal Conversion
def bin_to_dec(bin_str):
  binary_string = str(bin_str)
  bin_to_list = list(binary_string)
  value = 0

  for num in range(len(bin_to_list)):
    digit = bin_to_list.pop()
    if digit == '1':
      value = value + pow(2, num)
  
  return value

def binary_check_one():
  num_one_input = input("Enter your Binary Number: ")
  bin_input = ''

  if num_one_input.isnumeric():
    for num in num_one_input:
      if int(num) <= -1 or int(num) >= 2:
        bin_input = ''
        print("Invalid Binary, please use the digits 1 and 0")
        binary_check_one()
      else:
        bin_input = bin_input + str(num)
  else:
    print("Not valid Binary, please try again utilizing digits of 1 and 0")
    binary_check_one()

  return bin_input

def binary_check_two():
  num_two_input = input("Enter your second Binary Number: ")
  bin_input = ''

  if num_two_input.isnumeric():
    for num in num_two_input:
      if int(num) <= -1 or int(num) >= 2:
        bin_input = ''
        print("Invalid Binary, please use the digits 1 and 0")
        binary_check_two()
      else:
        bin_input = bin_input + str(num)
  else:
    print("Not valid Binary, please try again utilizing digits of 1 and 0")
    binary_check_two()

  return bin_input

def decimal_check():
  num_input = input("Enter a Decimal Number (0-255): ")

  if not num_input.isnumeric() or int(num_input) < 0 or int(num_input) > 255:
    print("Invalid Decimal, please use the digits 0 to 255")
    decimal_check()
  else:
    return int(num_input)
  
def binary_input():
  while True:
    print(
      """
        *** Binary Calculator *** \n
        ------------------------------
        (B)inary to Decimal Conversion
        (D)ecimal to Binary Conversion
        (A)dd two Binary Numbers
        (S)ubtract two Binary Numbers
        (M)ultiply two Binary Numbers
        D(i)vide two Binary Numbers
        (Q)uit
      """
    )

    user_input = input().lower()

    if user_input == 'b':
      get_decimal = bin_to_dec(binary_check_one())
      print(f"The Decimal Number is {get_decimal}")
      #bin_to_dec
    elif user_input == 'd':
      get_bin = dec_to_bin(decimal_check())
      print(f"The Binary Number is {get_bin}")
      # binary_check_two()# Will need refactoring and conditions to check if num in range
    elif user_input == 'a':
      addition = bin_add(binary_check_one(), binary_check_two())
      print(f"The binary results when added together are {addition}")
    elif user_input == 's':
      subtraction = bin_subtract(binary_check_one(), binary_check_two())
      print(f"The binary results when subtracted together are {subtraction}")
    elif user_input == 'm':
      multiply =  bin_multiply(binary_check_one(), binary_check_two())
      print(f"The binary results when multiplied together are {multiply}")
    elif user_input == 'i':
      divide = bin_divide(binary_check_one(), binary_check_two())
      print(f"The binary results when divided together are {divide}")
    elif user_input == 'q':
      print('Good Bye!')
      break

binary_input()
