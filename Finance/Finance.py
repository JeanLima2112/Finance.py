from openpyxl import Workbook,load_workbook

tabela = load_workbook("Base_Dados.xlsx")
aba_ativa = tabela.active
aba_ativa("B")