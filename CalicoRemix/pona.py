cases = int(input())

for c in range(cases):
    consonants = {"m","n","p","t","k","s","w","j","l"}
    vowels = {"a","e","i","o","u"}
   
    invalid1 = {"wu", "wo", "ji", "ti"}
    invalid2 = {"nn", "nm"}
    w = input()
   
    good = True
   
    for i in range(len(w)-1):
        index = []
        if w[i] in vowels:
            if w[i+1] in vowels:
                good = False
                break
        elif w[i] in consonants:
            if w[i+1] in vowels and w[i:i+2] not in invalid1:
                continue
            elif w[i+1] in consonants and w[i:i+2] not in invalid2 and w[i] == "n":
                continue
            else:
                good = False
                break
        else:
            good = False
            break
           
    if not (w[-1] in vowels or w[-1] == "n"):
        good = False
   
   
    if good and w!="n":
        print("pona")
    else:
        print("ike")
