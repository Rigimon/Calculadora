print ("Calculadora");
n1 = input();
n2 = input();
print();
print ("Calculadora");
print();
print ("(1)Soma");
print ("(2)Subtração");
print ("(3)Multiplicação");
print ("(4)Divisão");
op = input();
if op == 1:
    print (n1,"+",n2,"=",n1+n2);
elif op == 2:
    print (n1-n2);
elif op == 3:
    print (n1*n2);
elif (op == 4):
    print (n1/n2);
else:
    print ("Digite o numero certo fdp");
