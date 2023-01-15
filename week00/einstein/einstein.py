def main():
    mass = int(input("m: "))
    print(f"E: {equation(mass)}")

def equation(m):
    E = m * 300000000 ** 2
    return E

main()