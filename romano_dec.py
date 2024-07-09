def romano_para_decimal(romano):
    # Dicionário que mapeia símbolos romanos para seus valores inteiros correspondentes
    valores_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0  # Armazena o valor total da conversão
    anterior = 0  # Armazena o valor do símbolo romano anterior
    
    # Percorre o número romano do fim para o começo
    for char in romano[::-1]:
        valor = valores_romanos[char]  # Obtém o valor do símbolo romano atual
        
        # Se o valor atual é menor que o valor anterior, subtrai o valor atual do total
        if valor < anterior:
            total -= valor
        else:
            # Caso contrário, adiciona o valor atual ao total
            total += valor
        
        # Atualiza o valor anterior para o próximo loop
        anterior = valor
    
    return total  # Retorna o valor total convertido para decimal

def decimal_para_romano(decimal):
    # Lista de tuplas que mapeia valores inteiros para seus símbolos romanos correspondentes
    valores_romanos = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    resultado = ''  # Armazena o resultado da conversão
    
    # Percorre cada par (valor, símbolo) na lista de valores romanos
    for valor, simbolo in valores_romanos:
        # Enquanto o valor decimal for maior ou igual ao valor atual
        while decimal >= valor:
            resultado += simbolo  # Adiciona o símbolo romano ao resultado
            decimal -= valor  # Subtrai o valor correspondente do decimal
    
    return resultado  # Retorna o resultado convertido para romano

def main():
    while True:
        # Solicita a entrada do usuário
        entrada = input("Digite um número romano ou decimal (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break  # Encerra o loop se o usuário digitar 'sair'
        
        if entrada.isdigit():
            # Se a entrada for um número decimal
            decimal = int(entrada)  # Converte a entrada para inteiro
            resultado = decimal_para_romano(decimal)  # Converte o número decimal para romano
            print(f"O número decimal {decimal} em romano é: {resultado}")
        else:
            # Se a entrada for um número romano
            try:
                resultado = romano_para_decimal(entrada.upper())  # Converte o número romano para decimal
                print(f"O número romano {entrada.upper()} em decimal é: {resultado}")
            except KeyError:
                # Exibe uma mensagem de erro se o número romano for inválido
                print("Por favor, digite um número romano válido.")

if __name__ == "__main__":
    main()  # Executa a função principal se o script for executado diretamente
