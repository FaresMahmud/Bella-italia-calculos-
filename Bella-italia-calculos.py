
#DADOS DE ENTRADA 

QUANTIDADE = 4000          # potes produzidos no mês
PRECO_VENDA = 25.00        # R$ por pote

# Custos Variáveis (por unidade produzida)
insumos_base          = 6.00   # leite, creme de leite e insumos base
embalagens            = 1.50   # pote + tampa
energia_eletrica      = 0.50   # energia da fábrica por unidade

# Custos Fixos (mensais – não oscilam com produção)
aluguel_galpao        = 8_000.00
salarios_producao     = 12_000.00
depreciacao_maquinas  = 2_000.00

# Despesas (não relacionadas à produção)
prolabore             = 6_000.00   # despesa fixa
marketing             = 3_000.00   # despesa fixa
comissao_por_pote     = 1.00       # despesa variável por pote vendido


#CÁLCULOS 

cvu = insumos_base + embalagens + energia_eletrica

custo_fixo_total = aluguel_galpao + salarios_producao + depreciacao_maquinas

cfu = custo_fixo_total / QUANTIDADE

custo_total_por_pote = cvu + cfu

despesas_fixas = prolabore + marketing

despesas_variaveis_total = comissao_por_pote * QUANTIDADE

margem_contribuicao = PRECO_VENDA - cvu - comissao_por_pote

pec = (custo_fixo_total + despesas_fixas) / margem_contribuicao

receita_total = PRECO_VENDA * QUANTIDADE

custo_mes = (cvu * QUANTIDADE) + custo_fixo_total + despesas_fixas + despesas_variaveis_total

lucro_liquido = receita_total - custo_mes



linha = "-" * 52

print(linha)
print("  BELLA ITÁLIA – RELATÓRIO DE CUSTOS MENSAL")
print(linha)
print(f"  Quantidade produzida : {QUANTIDADE:>10,} potes")
print(f"  Preço de venda       : R$ {PRECO_VENDA:>10.2f}")
print(linha)

print("\n  CLASSIFICAÇÃO DOS GASTOS")
print(f"  {'Gasto':<36} {'Classificação'}")
print("  " + "-" * 50)
gastos = [
    ("Insumos base (leite, creme...)",     "Custo Variável"),
    ("Embalagens (pote e tampa)",           "Custo Variável"),
    ("Energia elétrica da fábrica",         "Custo Variável"),
    ("Aluguel do galpão",                   "Custo Fixo"),
    ("Salários equipe de produção",         "Custo Fixo"),
    ("Depreciação das máquinas",            "Custo Fixo"),
    ("Pró-labore do Sr. Lorenzo",           "Despesa Fixa"),
    ("Comissão dos vendedores",             "Despesa Variável"),
    ("Marketing e anúncios locais",         "Despesa Fixa"),
]
for nome, classe in gastos:
    print(f"  {nome:<36} {classe}")

print(f"\n{linha}")
print("  CÁLCULO DO CUSTO DO PRODUTO")
print(linha)
print(f"  CVU total (insumos+embal+energia) : R$ {cvu:>7.2f} / pote")
print(f"  Custo Fixo Total                  : R$ {custo_fixo_total:>10,.2f}")
print(f"  Custo Fixo Unitário (÷ {QUANTIDADE})   : R$ {cfu:>7.2f} / pote")
print(f"  Custo Total por Pote              : R$ {custo_total_por_pote:>7.2f} / pote")

print(f"\n{linha}")
print("  MARGEM DE CONTRIBUIÇÃO E PEC")
print(linha)
print(f"  Preço de Venda                : R$ {PRECO_VENDA:>7.2f}")
print(f"  (–) CVU                       : R$ {cvu:>7.2f}")
print(f"  (–) Despesas Variáveis/un     : R$ {comissao_por_pote:>7.2f}")
print(f"  = Margem de Contribuição (MC) : R$ {margem_contribuicao:>7.2f}")
print()
print(f"  Custos Fixos + Despesas Fixas : R$ {custo_fixo_total + despesas_fixas:>10,.2f}")
print(f"  PEC = {custo_fixo_total + despesas_fixas:,.0f} ÷ {margem_contribuicao:.2f}")
print(f"  Ponto de Equilíbrio Contábil  : {pec:>7.0f} potes")

print(f"\n{linha}")
print("  RESULTADO DO MÊS (4.000 potes)")
print(linha)
print(f"  Receita Total                 : R$ {receita_total:>10,.2f}")
print(f"  (–) Custo Total do Mês        : R$ {custo_mes:>10,.2f}")
print(f"  = Lucro Líquido               : R$ {lucro_liquido:>10,.2f}")
print(linha)
