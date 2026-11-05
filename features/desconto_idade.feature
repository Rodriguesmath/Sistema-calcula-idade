Feature: Cálculo de Desconto por Idade e Ocupação
  Como cliente da loja
  Quero receber descontos de acordo com minha idade e ocupação (estudo e trabalho)
  Para pagar um valor justo na compra do produto

  Scenario: Menor de 18 anos que apenas estuda recebe 5% de desconto
    Given que o sistema de cálculo de descontos está pronto com produto no valor de 100.00
    When informo a idade 16, estuda "sim" e trabalha "não"
    Then o desconto aplicado deve ser de 5% e o valor final deve ser 95.00

  Scenario: Menor de 18 anos que estuda e trabalha recebe 8% de desconto
    Given que o sistema de cálculo de descontos está pronto com produto no valor de 100.00
    When informo a idade 17, estuda "sim" e trabalha "sim"
    Then o desconto aplicado deve ser de 8% e o valor final deve ser 92.00

  Scenario: Pessoa entre 18 e 60 anos que apenas estuda não recebe desconto
    Given que o sistema de cálculo de descontos está pronto com produto no valor de 100.00
    When informo a idade 25, estuda "sim" e trabalha "não"
    Then o desconto aplicado deve ser de 0% e o valor final deve ser 100.00

  Scenario: Pessoa entre 18 e 60 anos que estuda e trabalha recebe 15% de desconto
    Given que o sistema de cálculo de descontos está pronto com produto no valor de 100.00
    When informo a idade 30, estuda "sim" e trabalha "sim"
    Then o desconto aplicado deve ser de 15% e o valor final deve ser 85.00

  Scenario: Pessoa com mais de 60 anos recebe 10% de desconto
    Given que o sistema de cálculo de descontos está pronto com produto no valor de 100.00
    When informo a idade 65, estuda "não" e trabalha "não"
    Then o desconto aplicado deve ser de 10% e o valor final deve ser 90.00

  Scenario: Tentar calcular desconto com idade inválida (negativa)
    Given que o sistema de cálculo de descontos está pronto com produto no valor de 100.00
    When tento informar uma idade inválida -5
    Then uma mensagem de erro "Insira uma idade válida" deve ser exibida
