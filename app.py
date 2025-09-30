from classess import*


pro1= Processador('a', 10)
pro2= Processador('b', 20)
pro3= Processador('c', 30)
pro4= Processador('d', 40)

mem1= Memoria_RAM(20,'static')
mem2= Memoria_RAM(10, 'dynamic')

arma1= Armazenamento('SSD',10)
arma2= Armazenamento('HDD',20)

com1= Computador('del', '1', 'a', 10 ,11, 'static','SSD',40,)
com2= Computador('del', '1', 'b',20,22,'dynamic', 'SSD',30)
com3= Computador('del', '1', 'c',30,33, 'static', 'HDD',20)
com4= Computador('del', '1', 'd',40,44, 'dynamic', 'HDD',10)

resp= int(input("--->"))
match resp:
    case 1:
        print(com1)