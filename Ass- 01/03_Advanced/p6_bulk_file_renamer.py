import os

def main():
    i = 0
    path = r"C:\Users\Hp\OneDrive\画像\screen shot\New folder\\" # r is fo raw string 
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        my_source = os.path.join(path, filename)  #original k path   
        my_dest = os.path.join(path, my_dest)     #new path
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()
