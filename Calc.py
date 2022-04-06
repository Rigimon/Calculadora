print ("Calculadora");
n1 = int(input());
n2 = int(input());
print();
print ("Calculadora");
print();
print ("(1)Soma");
print ("(2)Subtração");
print ("(3)Multiplicação");
print ("(4)Divisão");
op = int(input());
if op == 1:
    print (n1,"+",n2,"=",n1+n2);
elif op == 2:
    print (n1,"-",n2,"=",n1-n2);
elif op == 3:
    print (n1,"*",n2,"=",n1*n2);
elif (op == 4):
    print (n1,"/",n2,"=",n1/n2);
else:
    print ("Digite o numero certo fdp");
