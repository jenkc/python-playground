# exercise 3.1
def right_justify(string):
    justified = ' ' * (70 - len(string)) + string
    return justified

# exercise 3.2
def do_twice(function, value):
    function(value)
    function(value)
    
def print_twice(string):
    print(string)
    print(string)
    
# exercise 3.2


print(right_justify('hello'))
do_twice(print_twice, 'spam')