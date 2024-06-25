L={"One","Two","Three","Four","Five"}
with open("Question8.txt","w") as file :
    for item in L :
        file.write(f"{item},{len(item)}\n")