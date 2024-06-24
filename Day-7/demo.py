import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok, we will create instance for you")
else:
    print("not a valid option")

#using elif

type = sys.argv[1]

if type == "t2.micro":
    print("ok, it will cost 2 dollar")
elif type == "t3.medium":
    print("This will  cost 4 dollar")
elif type == "t2.xlarge":
    print("This will cost 8 dollar")
else:
    print("not a valid option")