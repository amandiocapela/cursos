print("Digite dois números:")
X = int(input())
Y = int(input())

while X != Y:
    if X < Y:
        print("Crescente!")
    else:
        print("Decrescente!")
    print("Digite dois números:")
    X = int(input())
    Y = int(input())