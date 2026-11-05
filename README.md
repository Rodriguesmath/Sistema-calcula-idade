# Sistema de Cálculo de Descontos por Idade — Testes com BDD

> **Instituição:** Instituto Federal da Paraíba (IFPB) — Campus Campina Grande  
> **Disciplina:** Testes de Software — Cap. 4: Cenários e Casos de Testes com BDD  
> **Professor:** Breno Romero  

---

## 1. Sobre o BDD (Behavior-Driven Development)

O **BDD (Desenvolvimento Orientado a Comportamento)** é uma prática de desenvolvimento ágil voltada a alinhar desenvolvedores, analistas de negócios (QA) e *stakeholders* em torno do **comportamento esperado do software** sob o ponto de vista do usuário, em vez de focar apenas em especificações puramente técnicas.

### Principais Vantagens Aplicadas neste Projeto
- **Melhor Desenvolvimento:** Descreve o que é esperado da funcionalidade na visão do cliente, permitindo implementar a lógica mais limpa em Python.
- **Maior Interação entre Áreas:** Regras escritas em linguagem natural estruturada (**Gherkin**), compreensíveis por pessoas técnicas e não técnicas.
- **Documentação Dinâmica e Testes Mais Baratos:** Os mesmos cenários `.feature` servem como documentação viva de requisitos e como especificação executável automatizada via `behave`.

---

## 2. Aplicação das 4 Fases do BDD

### Fase 1: Descoberta (*Discovery* e Mapeamento de Exemplos)

**História de Usuário (*User Story*):**
> *"Como **cliente da loja**, quero **calcular o desconto do produto com base na minha idade e ocupação (estudo/trabalho)** para que **eu pague um valor justo conforme meu perfil**."*

#### Mapeamento de Exemplos (*Example Mapping*)

| Exemplo | Breve Descrição | Regras ou Restrições | Resultado Esperado (Produto = R$ 100,00) | Dúvidas / Incertezas Resolvidas |
| :--- | :--- | :--- | :--- | :--- |
| **CT01 — Jovem Estudante** | Cliente com 16 anos que apenas estuda | `< 18` anos e `estuda = True` (`trabalha = False`) | **5% de desconto** (`R$ 95,00`) | Menor que não estuda não recebe desconto |
| **CT02 — Jovem Aprendiz** | Cliente com 17 anos que estuda e trabalha | `< 18` anos, `estuda = True` e `trabalha = True` | **8% de desconto** (`R$ 92,00`) | Desconto de 8% substitui o de 5% (não acumula) |
| **CT03 — Adulto Estudante** | Cliente com 25 anos que apenas estuda | Entre `18` e `60` anos, `estuda = True` e `trabalha = False` | **0% de desconto** (`R$ 100,00`) | Limites 18 e 60 são inclusivos |
| **CT04 — Adulto Trabalhador-Estudante** | Cliente com 30 anos que estuda e trabalha | Entre `18` e `60` anos, `estuda = True` e `trabalha = True` | **15% de desconto** (`R$ 85,00`) | Exige ambas as condições simultaneamente |
| **CT05 — Idoso** | Cliente com 65 anos | `> 60` anos (independente de estudo ou trabalho) | **10% de desconto** (`R$ 90,00`) | Não há necessidade de perguntar ocupação no CLI |
| **CT06 — Idade Inválida** | Entrada de idade negativa (`-5`) | `idade < 0` | Mensagem: `"Insira uma idade válida"` | Bloqueia o cálculo imediatamente |

---

### Fase 2: Definição (Regras de Negócio e Critérios de Aceitação)

1. **RN01:** Se a pessoa tem **menos que 18 anos** e **é estudante**, tem desconto de **5%**.
2. **RN02:** Se a pessoa tem **menos que 18 anos** e **estuda e trabalha**, tem desconto de **8%**.
3. **RN03:** Se a pessoa tem **entre 18 e 60 anos** e **só estuda**, **não tem desconto (0%)**.
4. **RN04:** Se a pessoa tem **entre 18 e 60 anos** e **estuda e trabalha**, tem desconto de **15%**.
5. **RN05:** Se a pessoa tem **mais que 60 anos**, tem desconto de **10%**.
6. **RN06:** Idades negativas (`< 0`) devem ser rejeitadas com a mensagem `"Insira uma idade válida"`.

---

### Fase 3: Formalização / Formulação em Gherkin (`Given-When-Then` / `Dado-Quando-Então`)

Seguindo a estrutura **Local (`Given/Dado`) – Ações (`When/Quando`) – Resultado (`Then/Então`)**, os cenários foram formalizados em [`features/desconto_idade.feature`](features/desconto_idade.feature):

```gherkin
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
```

#### Equivalência em Português (`Dado-Quando-Então`)
- **Dado** que o sistema de cálculo de descontos está pronto com produto no valor de `100.00`
- **Quando** informo a idade `<idade>`, estuda `"<sim/não>"` e trabalha `"<sim/não>"`
- **Então** o desconto aplicado deve ser de `<X>%` e o valor final deve ser `<valor_final>`

---

### Fase 4: Entrega e Automação dos Testes

A automação foi construída em Python utilizando o framework **Behave** ([`features/steps/desconto_steps.py`](features/steps/desconto_steps.py)) integrado ao módulo principal ([`idade.py`](idade.py)).

#### Estrutura do Repositório
```text
Sistema-calcula-idade/
├── idade.py                           # Regra de negócio e interface CLI
├── requirements.txt                   # Dependência do framework BDD (behave)
├── README.md                          # Documentação completa de testes BDD
└── features/
    ├── desconto_idade.feature         # Especificação Gherkin dos cenários
    └── steps/
        └── desconto_steps.py          # Automação dos passos Given/When/Then
```

#### Como Executar

1. **Executar o sistema via terminal (interativo):**
   ```bash
   python3 idade.py
   ```

2. **Executar a suíte automatizada de testes BDD:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   behave
   ```

#### Resultado da Execução Automatizada
```text
1 feature passed, 0 failed, 0 skipped
6 scenarios passed, 0 failed, 0 skipped
18 steps passed, 0 failed, 0 skipped
```
