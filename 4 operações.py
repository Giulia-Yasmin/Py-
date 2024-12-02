x = int(input ("insira um valor: "))
y = int(input ("insira um valor: "))
operação= int(input ("adição=1 ou subtração=2 ou multiplicação=3 ou divisão=4: "))

if operação==1:
    l=(x + y)
if operação==2:
    l=(x - y)
if operação==3:
    l=(x * y)
if operação==4: 
    l=(x / y)
print ('resultado: ' + str(l))
