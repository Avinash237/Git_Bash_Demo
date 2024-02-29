"""
print Alphabet and pattern letters

"""

asciinumber = 65
for i in range(0,7):
    for j in range(0,i + 1):
        character = chr(asciinumber)
        print(character,end=' ')
        asciinumber += 1
    print(" ")