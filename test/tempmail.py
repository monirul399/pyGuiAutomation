import pyperclip

tempMails = []
with open("../storage/tempMail.txt") as file:
    for line in file:
        line = line.strip('\n')
        line = line.strip(' ')
        tempMails.append(line)

str = pyperclip.paste()
index = tempMails.index(str)

if index == (len(tempMails) - 1):
    print(tempMails[0])
else:
    print(tempMails[index + 1])