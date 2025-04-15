LOW = 2
HIGH= 10

def in_range(n , low= LOW , high= HIGH):

    if n >= low and n <= high:
        return True
    else:
        return False
    
def main():

    n = int(input("Enter a number: "))
    print(in_range(n))

main()