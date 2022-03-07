f = open("C:/Users/82102/Desktop/KAIST_22/CS101/2021/planets.txt", "r")

planets = []
for l in f:
    planets.append(l.strip())

print(planets)

#위의 과정을 걍 한 줄로
planets2 = []
planets2 = f.readlines()
print(planets2)
f.close()

f2 = open("C:/Users/82102/Desktop/KAIST_22/CS101/2021/planets.txt", "r")
current = 0
earth = 0
for planet in f2:
    if planet.strip().lower() == 'earth':
        print(earth+1)
        break
    else:
        earth += 1

def alphabetian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True

print(alphabetian("abdf"))
print(alphabetian("abtdf"))

def triple_double(word):
    for i in range(len(word)-5):
        if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
            return True
    return False

print(triple_double("bookkeeper"))
print(triple_double("Mississippi"))