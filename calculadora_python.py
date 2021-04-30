#calculadora python

x=int(input("Digite o primeiro número: "))
operacao=input("Digite a operação desejada( +, -, x, /): ")
y=int(input("Digite o segundo número: "))
print("\n")




if operacao=="+":
    print(x, " + ", y, " = ", x+y)

elif operacao=="-":
	print(x, " - ", y, " = ", x-y)

elif operacao=="x":
	
	print(x, " x ", y, " = ", x*y)

elif operacao=="/" and y!=0:
	
	print(x, " / ", y, " = ", x/y)
    
else:
    print("Operação invalida")
        
	