yoko = int(input('行数を入力してください'))
tate = int(input('列数を入力してください'))

for miu in range (1, yoko + 1):
    for ra in range(1, tate + 1):
        print(miu*ra, end=" ")
    
    print("\n", end="")

