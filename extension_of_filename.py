filename = input("Input the Filename: ")
f_extns = filename.split(".")
my_dict = {"c":"C","cpp":"C++","py":"Python","java":"Java"}
print ("The extension of the file is : " + my_dict[f_extns[-1]])
