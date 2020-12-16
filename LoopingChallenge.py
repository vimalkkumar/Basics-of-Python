# Create a program that takes an IP address at the keyboard and validate that
# it can be interpreted as a valid address.
# An IP address consists of 4 numbers, separated from each other with full stop.
# Each number can have no more than 3 digits.
# Examples are:
# # 127.0.0.1
# # 192.168.0.1
# # 10.0.12.255
# # 172.16.57.1
# # 255.255.255.0
#
# If the IP address is valid, print the word "ping" followed by the IP address otherwise print a
# suitable error message -
# As an optional extra part to the challenge, restrict each number to be between 0 and 255, and do not
# allow 0.0.0.0 as a valid address.
# Once you have a working program, here are some suggestion for invalid input to test:
# # .123.45.678.91
# # 123.4567.8.9
# # 123.156.289.10123456
# # .10.10t.10.10
# # 12.9.34.6.12.90
# # '' - that is, press enter without typing anything
#

ipAddress = input('Please enter an IP Address : ')

number = ''
position = 1
segment = 1
total = 0
errorMessage = ''

for digit in ipAddress:
    if digit != '.':
        # we have not got a full stop, sp we have digit
        if digit in '0123456789':
            number += digit
        else:
            errorMessage = 'Error in position {} in section {}, invalid character {}'.format(position, segment, digit)
            break
    else:
        # We have a full stop, check the length of the number that we have built up so far
        if (len(number) == 0) or (len(number) > 3):
            errorMessage = 'Error near position {} in section {}, ' \
                           'each number must be 1 to 3 digits'.format(position, segment)
            break
        currentValue = int(number)
        if currentValue > 255:
            errorMessage = "Error near position {} in section {}," \
                           " {} is too large".format(position, segment, currentValue)
            break
        total += currentValue
        number = ''
        segment += 1
        if segment > 4:
            errorMessage = 'Error near position {}, IP address must contains ' \
                           'more than 4 segments'.format(position)
    position += 1
else:
    if (len(number) == 0) or (len(number) > 3):
        errorMessage = 'Error near position {}, in section {}, each number' \
                       ' must contains 1 tp 3 digits'.format(position, segment)
    elif int(number) > 255:
        errorMessage = "Error near position {}, in section {}, " \
                       "{} is too long".format(position, segment, number)
    elif total + int(number) == 0:
        errorMessage = "Error: IP Address segments cannot all be zero"
    elif position > 16:
        errorMessage = 'Error : IP address can not more than 15 characters, found {}'.format(position)
    elif segment != 4:
        errorMessage = 'Error near position {}, IP address contains {} segments, ' \
                       '4 required'.format(position, segment)
    else:
        print('ping {}'.format(ipAddress))

if errorMessage:
    print(ipAddress)
    print(" " * (position - 1) + "^")
    print(errorMessage)
