def romano_para_decimal(romano):
    # Dicionário de valores romanos
    valores_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    anterior = 0
    
    # Percorre o número romano do fim para o começo
    for char in romano[::-1]:
        valor = valores_romanos[char]
        
        # Se o valor atual é menor que o anterior, subtrai
        if valor < anterior:
            total -= valor
        else:
            total += valor
        
        anterior = valor
    
    return total

def main():
    while True:
        entrada = input("Digite um número romano (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break
        try:
            resultado = romano_para_decimal(entrada.upper())
            print(f"O número romano {entrada.upper()} em decimal é: {resultado}")
        except KeyError:
            print("Por favor, digite um número romano válido.")

if __name__ == "__main__":
    main()
