def expandir_intervalos(entrada):
    partes = entrada.split()
    resultado = []
    i = 0
    while i < len(partes):
        if partes[i] == 'à':
            if i > 0 and i + 1 < len(partes):
                try:
                    inicio = int(partes[i - 1])
                    fim = int(partes[i + 1])
                    resultado.pop()  # Remove o número inicial
                    resultado.extend(range(inicio, fim + 1))
                    i += 1  # Avança para o número final (o loop incrementará i novamente)
                except ValueError:
                    print("Erro: Entrada inválida. Certifique-se de que os números são inteiros.")
                    return []
            else:
                print("Erro: Formato de entrada inválido para o intervalo 'a'.")
                return []
        else:
            try:
                resultado.append(int(partes[i]))
            except ValueError:
                print("Erro: Entrada inválida. Certifique-se de que os números são inteiros.")
                return []
        i += 1
    return resultado

entrada = input()
resultado = expandir_intervalos(entrada)

# Processa a lista resultante para remover duplicatas consecutivas criadas por 'a'
if resultado:
    resultado_final = [resultado[0]]
    for i in range(1, len(resultado)):
        if resultado[i] != resultado[i-1]:
            resultado_final.append(resultado[i])
        print(resultado_final[i])