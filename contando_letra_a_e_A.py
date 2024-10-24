while True:

    print("Vamos contar quantas vezes a letra 'A' aparece\n")
    string = input("Digite uma palavra ou frase: ")

    if not string:
        print("\nVocê não digitou nada. Por favor, insira algum texto\n")

    elif string.isdigit():
        print('\nVoce digitou apenas números. Por favor, insira palavras\n')

    else:

        string_lower = string.lower()
        total_a = string_lower.count('a')

        if total_a > 0:
            print(f"\nA letra 'A' aparece {total_a} vezes\n")
        else:
            print(f"\nA letra 'A' não apareceu nenhuma vez em sua palavra ou frase\n")
