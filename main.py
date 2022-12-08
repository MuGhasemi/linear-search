print("for exit of loop, enter <exit> in input")
list_search=[]
while True:
    text = input("Pls Enter : ")
    if text == "exit":
        break
    elif text == " " or text == "":
        continue
    else:
        list_search.append(text)

number=0
count=0
c=0
for i in range(len(list_search)):
    for j in range(i,len(list_search)):
        if list_search[j]==list_search[i]:
            c+=1
    if c>=count:
        count=c
        number=list_search[i]
    c=0
print(list_search)
print(f"in list {count} number -> {number} exist ...")