from sympy import *
incX=[]             #incógnita x
incY=[]             #incógnita y
delta=[[]]          #Lista que contém listas, primeira camada é o número do delta, a segunda os seus conteúdos
                    #Ex: Delta[0][0] = primeiro conteúdo do delta1
x = symbols('x')    #função para utilizar o x como um símbolo

### Função para calcular cada valor de delta
def calcdeltas(numdelta):
  for i in range(tam):
    if i<tam-1 and len(delta)<=1:                                     #Para o delta 1
      delta[numdelta].append((incY[i+1]-incY[i])/(incX[i+1]-incX[i])) #Adiciona o valor na lista dentro do delta[0]
      """
                      y(1)-y(0)
      Delta1(0) =     --------- quando o i = 0
                      x(1)-x(0)

      """
      print(delta[numdelta][i])

    elif i<tam-len(delta) and len(delta)>1:    #Para os demais deltas
      delta[numdelta].append((delta[len(delta)-2][i+1]-delta[len(delta)-2][i])/(incX[len(delta)+i]-incX[i])) #Adiciona o valor na lista dentro do delta[numdelta]
      """
                   Delta1(1)-Delta1(0)
      Delta2 (0) = -------------------   quando len(delta)=2 e i=0
                        x(2)-x(0)
      """
      print(delta[numdelta][i])

### Input para os valores
tam=int(input("Digite a quantidade de pontos: "))
for i in range(tam):                                        #for que roda "tam" vezes
  incX.append(float(input(f"Digite o valor de X{i}: ")))    #transforma o valor do input de string para float e
  incY.append(float(input(f"Digite o valor de Y{i}: ")))    #o adiciona a lista

### Loop para pegar cada "camada" do delta (delta1, delta2...)
for i in range(tam-1):
  print(f"Valores de Delta {i+1}:")
  calcdeltas(i)                         #chama a função calcdeltas
  delta.append([])                  #aumenta o tamanho da lista "delta"
delta.pop()                         #remove o último elemento da lista "delta" que esta vazio ao sair do loop

### Calcular o polinômio
f=incY[0]                           #cria uma variavel para a função do polinomio, que começa com o valor do y(0)
aux=1                               #variavel auxiliar da função
for i in range(len(delta)):         #loop que roda o tamanho do delta vezes
  for i in range(len(delta[i])):    #loop que roda o tamanho da lista dentro do delta[i] vezes
    aux=aux*(x-incX[i])             #auxiliar recebe aux*(x-x(i))
  f=f+aux*delta[i][0]               #atualiza o valor de f para f+auxiliar
  aux=1                             #reseta o auxiliar

f=simplify(f)                       #função para simplificar o "f"
print(f"Polinômio: {f}")

