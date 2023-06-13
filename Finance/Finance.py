from openpyxl import load_workbook

tabela = load_workbook("Base_Dados.xlsx")
ws = tabela["Gastos(Dia)"]
for c in ws.values:
    print(c)
    #for value in c:
        #print(value)