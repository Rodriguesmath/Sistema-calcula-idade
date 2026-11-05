def calcular_desconto(idade: int, estuda: bool = False, trabalha: bool = False) -> float:
    if idade < 0:
        raise ValueError("Insira uma idade válida")
    if idade > 60:
        return 0.10
    if idade < 18 and estuda:
        return 0.08 if trabalha else 0.05
    if 18 <= idade <= 60 and estuda and trabalha:
        return 0.15
    return 0.0


def calcular_valor_final(
    idade: int,
    estuda: bool = False,
    trabalha: bool = False,
    valor_produto: float = 100.0,
) -> float:
    desconto = calcular_desconto(idade, estuda, trabalha)
    return round(valor_produto * (1 - desconto), 2)


def main() -> None:
    idade = int(input("Digite a sua idade: "))
    valor_produto = 100.0

    if idade < 0:
        print("Insira uma idade válida")
        return

    if idade > 60:
        estuda = False
        trabalha = False
    else:
        estuda = input("Estuda? (s/n): ").strip().lower() == "s"
        trabalha = input("Trabalha? (s/n): ").strip().lower() == "s"

    desconto = calcular_desconto(idade, estuda, trabalha)
    valor_final = calcular_valor_final(idade, estuda, trabalha, valor_produto)

    if desconto > 0:
        print(f"CLIENTE COM DESCONTO ({int(desconto * 100)}%)!!! valor do produto: {valor_final:.2f}")
    else:
        print(f"valor do produto: {valor_final:.2f}")


if __name__ == "__main__":
    main()
