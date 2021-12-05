def teste():
    cpf = []
    for i in range(11):
        cpf.append (input('Digite um valor: '))
        int_list = list(map(int, cpf))
        
    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    global n7
    global n8
    global n9
    global n10
    global n11
    
    n1 = int_list[0]
    n2 = int_list[1]
    n3 = int_list[2]
    n4 = int_list[3]
    n5 = int_list[4]
    n6 = int_list[5]
    n7 = int_list[6]
    n8 = int_list[7]
    n9 = int_list[8]
    n10 = int_list[9]
    n11 = int_list[10]


    if (n1 == n2) and (n2 == n3) and (n3 == n4) and (n4 == n5) and  (n5 == n6 ) and (n6 == n7) and (n7 == n8) and (n8 ==  n9) and (n9 == n10) and (n10 == n11):
        print ('--------------------------------------------')
        print('cpf inválido por favor digite um cpf válido: ')
        print ('--------------------------------------------')
        teste()

def calculo_1():
    global soma_1
    global resto_1
    
    mult_1 = n1 * 10
    mult_2 = n2 * 9
    mult_3 = n3 * 8
    mult_4 = n4 * 7
    mult_5 = n5 * 6
    mult_6 = n6 * 5
    mult_7 = n7 * 4
    mult_8 = n8 * 3
    mult_9 = n9 * 2
    
    soma_1 =  mult_1 + mult_2 + mult_3 + mult_4 + mult_5 + mult_6 + mult_7 + mult_8 + mult_9
    resto_1 = (soma_1 * 10) % 11
    
    if (resto_1 == 10):
        resto_1 = 0
    

def calculo_2():
    global soma_2
    global resto_2
    
    mult_11 = n1 * 11
    mult_22 = n2 * 10
    mult_33 = n3 * 9
    mult_44 = n4 * 8
    mult_55 = n5 * 7
    mult_66 = n6 * 6
    mult_77 = n7 * 5
    mult_88 = n8 * 4
    mult_99 = n9 * 3
    resto_primeiro = resto_1 * 2
   
    soma_2 =  mult_11 + mult_22 + mult_33 + mult_44 + mult_55 + mult_66 + mult_77 + mult_88 + mult_99 + resto_primeiro
    resto_2 = (soma_2 * 10) % 11
    
    if (resto_2 == 10):
        resto_2 = 0

  
resposta = str(input('Deseja iniciar o programa (sim/não): '))
print ('-------------------------------------------')     
if (resposta == 'sim'):
    teste()
else:
    print('FIM DO PROGRAMA')

calculo_1()
calculo_2()

print ('---------------------------')

if (resto_1 == n10) and (resto_2 == n11):
    print ('Parabéns, seu cpf é válido')
else:
    print ('CPF INVÁLIDO')
print ('---------------------------')   
