import re


def askforname(msg):
    name = input(f"{msg}")
    if name.isalpha():
        if len(name) > 0:
            print(f"{name}: is valied name")
            return name
        return askforname
    return askforname(msg)


'''
+:One or more occurrences
*:Zero or more occurrences
[-]:Returns a match for any character in the range
\:Signals a special sequence
{}:Exactly the specified number of occurrences
'''


def isValid(msg):
    # used to compile a regular expression pattern provided as a string into a regex pattern object
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    email = input(f"{msg}")
    # returns a match object if and only if the entire string matches the pattern
    if re.fullmatch(regex, email):
        print(f"{email}: is Valid email")
        return email
    else:
        return isValid(msg)


askforname("Please enter ur name: ")
isValid("please Enter ur email: ")
