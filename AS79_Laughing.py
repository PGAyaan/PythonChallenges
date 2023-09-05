def make_it_laugh(input_string): #Define a list of vowels
    vowels = 'AEIOUaeiou'
    result = ''
    for char in input_string:
        if char in vowels:
            result += 'haha'
        else:
            result += char
    print(result)
  
input_string = "Replacing all the vowels test"
make_it_laugh(input_string)
