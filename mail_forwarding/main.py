

with open("../mail_forwarding/names.txt") as file:
    all_names = file.readlines()

with open("../mail_forwarding/messages.txt","r") as message:
    header = message.readline()
    body = message.readlines()


for name in all_names:
    x = header.replace("[name]", name)
    with open(f"../mail_forwarding/{name}.txt", "w") as new:
        new.write(x)
        for line in body[1:]:
            new.write(line)



