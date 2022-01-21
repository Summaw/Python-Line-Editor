import time

print(" _____            _  ")
print("|  __ \          | |    ")
print("| |  | |_   _  __| |____")
print("| |  | | | | |/ _` |_  /")
print("| |__| | |_| | (_| |/ / ")
print("|_____/ \__,_|\__,_/___|")
print(" Made By UmRange")
print("Remove Duplicated lines")

file = input('Please input the name of the file>> ')
start = time.time()

openFile = open(file, "r")
writeFile = open("RemovedDup.txt", "w")
sexyme = set()
x = 0
for txtLine in openFile:
    if txtLine not in sexyme:
        writeFile.write(txtLine)
        sexyme.add(txtLine)
    else:
        x += 1

openFile.close()
writeFile.close()
end = time.time()
e = end - start
print(f'\nUsed {e} Seconds to Clear Dupes,Cleared {x} Lines')
