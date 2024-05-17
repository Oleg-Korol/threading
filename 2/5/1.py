from concurrent.futures import ThreadPoolExecutor

bases = [3, 44, 22]
exponents = [12, 31]

def power(base, exponent):
    result =pow(base,exponent)
    return f"{base} в степени {exponent} равно {result}"

def main():
    with ThreadPoolExecutor(max_workers=len(bases)) as executor:
        data = list(zip(bases,exponents))
        print(data)
        resalts = executor.map(power,bases,exponents)
        [print(res) for res in resalts]
main()
