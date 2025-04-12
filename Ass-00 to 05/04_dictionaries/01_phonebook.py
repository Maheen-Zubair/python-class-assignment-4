# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_numbers():

    phonebook = {}                 

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):

    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()  #neww dictionary save in this variable
    print_phonebook(phonebook)        #pass value of phonebook,which we get in previous step
    lookup_numbers(phonebook)


main()