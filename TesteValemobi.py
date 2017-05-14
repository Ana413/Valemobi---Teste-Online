#BIBLIOTECAS
import MySQLdb
import os

#CONEXAO COM O BANCO
conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "valemobi") #Conexao com o banco

print "CLIENTES\n"

#SELECT NO BANCO - vl_total > 560 e id_customer entre 1500 e 2700 
cursor = conn.cursor()
cursor.execute ("SELECT * FROM tb_customer_account where vl_total > 560 and id_customer >=1500 and id_customer <=2700 order by vl_total") 

#VARIAVES PARA VALOR TOTAL E QUANTIDADE DE REGISTROS ENTRE AS ESPECIFICACOES NO SELECT
total = 0 
i = 0

#IMPRIME OS RESULTADOS 
for result in cursor:
	total += result[4]
	i+=1

	print 'Id: %1.2d	CPF: %13.15s	Nome: %2.13s	Status da Conta: %3.5s	 Valor Total: R$%2.2f ' % (result[0], result[1], result[2], result[3], result[4])

cursor.close()	

#CALCULO DA MEDIA
media = total / i
print("\nMEDIA DO SALDO: R$%.2f \n" % media)
conn.close()


os.system("pause")


