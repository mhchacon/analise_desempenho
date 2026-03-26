#1. Média aritmética
def media(lista):
  return ((sum(lista))/len(lista))

print(media([4, 8, 6, 2]))
print(media([1, 2, 3, 4]))
print(media([10, 20, 30, 40]))

print("---------------------------------------------")

#3. Contar palavras
def contarPalavras(lista):
  contador = 1
  for s in lista:
    if s == " ":
      contador += 1
  return contador

print(contarPalavras(("ola mundo cruel")))
print(contarPalavras(("ola mundocruel")))
print(contarPalavras(("teste teste teste teste")))

print("---------------------------------------------")

#5. Segundo maior elemento
def segundoMaior(lista):
  lista.remove(max(lista))
  return max(lista)

print(segundoMaior([3, 7, 2, 9, 5]))
print(segundoMaior([1, 20, 10, 11, -1]))
print(segundoMaior([0, 11, -3, 32, 22]))

print("---------------------------------------------")

# 6. Soma dos dígitos [recursão]
def soma(n):
  if n ==0:
    return 0
  else:
        return (n % 10) + soma(n // 10)

n = 1234
resultado = soma(n)
print(resultado)

print("---------------------------------------------")

#8. Maior elemento da matriz

def MaiorElemento(matriz):
  if not matriz: 
    return None 

  g = [elemento for row in matriz for elemento in row]
  
  return max(g)

n = [(3, 7), (2, 9), (5, 1)]
resultado = MaiorElemento(n) 
print(resultado)

print("---------------------------------------------")

# 11. Inverter palavras

def reverter_palavras(s: str) -> str:
    return " ".join(s.split()[::-1])

texto = "eu gosto de python"
print(reverter_palavras(texto))