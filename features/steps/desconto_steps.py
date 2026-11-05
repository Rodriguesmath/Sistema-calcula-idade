from behave import given, when, then
from idade import calcular_desconto, calcular_valor_final


@given("que o sistema de cálculo de descontos está pronto com produto no valor de {valor:f}")
def step_sistema_pronto(context, valor):
    context.valor_produto = valor
    context.erro = None


@when('informo a idade {idade:d}, estuda "{estuda_str}" e trabalha "{trabalha_str}"')
def step_informo_dados(context, idade, estuda_str, trabalha_str):
    estuda = estuda_str.strip().lower() == "sim"
    trabalha = trabalha_str.strip().lower() == "sim"
    context.desconto = calcular_desconto(idade, estuda, trabalha)
    context.valor_final = calcular_valor_final(
        idade, estuda, trabalha, context.valor_produto
    )


@when("tento informar uma idade inválida {idade:d}")
def step_idade_invalida(context, idade):
    try:
        calcular_desconto(idade)
    except ValueError as exc:
        context.erro = str(exc)


@then("o desconto aplicado deve ser de {percentual:d}% e o valor final deve ser {esperado:f}")
def step_verifica_desconto(context, percentual, esperado):
    assert round(context.desconto * 100) == percentual, (
        f"Esperado {percentual}%, obtido {round(context.desconto * 100)}%"
    )
    assert context.valor_final == round(esperado, 2), (
        f"Esperado {esperado:.2f}, obtido {context.valor_final:.2f}"
    )


@then('uma mensagem de erro "{mensagem}" deve ser exibida')
def step_verifica_erro(context, mensagem):
    assert context.erro == mensagem, f"Esperado '{mensagem}', obtido '{context.erro}'"
