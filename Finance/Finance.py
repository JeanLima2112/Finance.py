from openpyxl import load_workbook
Tent = Tsai = 0
tabela = load_workbook("Base_Dados.xlsx")
ws = tabela["Teste"]

for c in ws.values:
    print(c)
    if c[0] != "Entrada":
        Tent += c[0]
        Tsai += c[1]
print(f"O total de entradas é {Tent}")
print(f"O total de Saidas é {Tsai}")
print(f"O saldo é {Tent - Tsai}")
