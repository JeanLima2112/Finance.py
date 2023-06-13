tab = [['Cachorro Quente',100,1.20],
       ['Bauru Simples',101,1.30],
       ['Bauru com ovo',102,1.50],
       ['Hambúrguer',103,1.20],
       ['Cheeseburguer',104,1.30],
       ['Refrigerante',105,1.00]]
pedido = []
pedidoatual = []
total = 0
print("-"*32)
print(f"\033[7;31m{'CARDAPIO':^32}\033[m")
print("-"*32)
print(f"\033[7;31m{'Lanche':>10}{'COD':>13}{'Preço':>9}\033[m")
for c in range(0,len(tab)):
       print(f"{tab[c][0]:_<20}",end="")
       print(f"{tab[c][1]:_<6}",end="")
       print(f"R${tab[c][2]:>1.2f}")
print("-"*32)
while True:
       while True:
              ped = int(input("Digite o codigo do lanche desejado:"))
              if ped in [100,101,102,103,104,105]:
                     break
              print("Codigo de lanche invalido, Responda Novamente.",end=" ")
       while True:
              uni = int(input("Quantas unidades?:"))
              if uni > 0:
                     break
              print("Numero Invalido, Digite um numero Maior que 0.",end=" ")
       while True:
              resp = input("Deseja Finalizar o Pedido?[S/N]:").strip().upper()[0]
              if resp == "S" or resp == "N":
                     break
              print("Resposta Invalida,Responda Novamente.",end=" ")
       for c in range(0,len(tab)):
              if tab[c][1] == ped:
                     pedidoatual.append(tab[c][0])
                     pedidoatual.append(uni)
                     pedidoatual.append((tab[c][2] * uni))
                     pedido.append(pedidoatual[:])
                     pedidoatual.clear()
       if resp == 'S':
              print("-" * 32)
              print(f"\033[7;31m{'Pagamento':^32}\033[m")
              print("-" * 32)
              print(f"\033[7;31m{'Lanche':>9}{'QUANT':>12}{'Preço':>10}\033[m")
              for c in range(0,len(pedido)):
                     print(f"{pedido[c][0]:_<18}", end="")
                     print(f"{pedido[c][1]:_<6}", end="")
                     print(f"R${pedido[c][2]:>1.2f}")
                     total += pedido[c][2]
              print("-" * 32)
              print(f"\033[7;31m{'Total a Pagar':_<26}R${total:>1.2f}\033[m")
              print("-" * 32)
              break