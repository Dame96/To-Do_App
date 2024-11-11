# module 1 even or odd assingment on codewars
def even_or_odd(number):
    if number % 2 ==0: 
        return 'Even'
    else:
        return'Odd'
# Convert a Number to a String!
def number_to_string(num):
    return str(num)

# Vowel Count
def get_count(sentence):
    count = 0 
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        print(vowel,sentence.count(vowel))
        count += sentence.count(vowel)
        print(count)
    return(count)
    
       