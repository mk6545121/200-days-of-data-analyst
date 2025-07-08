#TODAY I LEARN ABOUT FILE HANDLING IN PYTHON
with open("file.txt",'r') as file:
    content=file.read()
    print(content.strip())

# with open("file.txt",'r') as file:
#     for line in file:     
#         print(line.strip())
# with open("file.txt",'r') as file:
#     lines = file.readlines()

#     for line in lines:
#         print(line.strip())
# with open("file.txt",'r') as file:
data =["manish,1200","ravi,2300","king,9000"]
for line in data:
    print(line.split(","))
    print(line.strip())


data =["manish,1200","ravi,2300","king,9000"]
for line in data:
    name,spend=line.split(",")
    print(f"{name} yOU spend {spend}")



with open("mytext.txt",'r') as file:
    data=file.readlines()
    for line in data:
        name, spend = line.strip().split(",")
        spend=int(spend)
        if spend>500:
            print(f"{name} you spend more tha rupees 500")
        else:
            continue


