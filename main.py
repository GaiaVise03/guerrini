import mysql.connector
#creo connessione con usr e pwd su db
dbconn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database ="db25_prova"
)
#tramite connessione creo un cursore per leggere dati
mycursor = dbconn.cursor()
#eseguo comandi sql con cursore
mycursor.execute("SELECT * FROM t_user")
#leggo tutti i record in una sola volta
myresult = mycursor.fetchall()
print(myresult)
print()
for currentrecord in myresult:
    print(currentrecord[2] + " " + currentrecord[1])

searchid=input("dimmi id utente: ")
cmdsql="select * from t_user where id_user=" +searchid
mycursor.execute(cmdsql)
utente=mycursor.fetchone()
print(utente)
print()
print(utente[2] + " " + utente[1] + " " + utente[3])
#creo cursore che ritorna dictionary
mycurdict=dbconn.cursor(dictionary=True)
mycurdict.execute(cmdsql)
utente=mycurdict.fetchone()
print()
print(utente)


nome=input("dimmi il nome: ")
cognome=input("dimmi il cognome: ")
mail=input("dimmi la mail: ")
pwd=input("dimmi la password: ")

inssql ="insert into t_user (firstname,lastname,mail,pwd) values ('" + nome + "','" + cognome + "','" + mail +"','" + pwd + "')"  
inscur=dbconn.cursor()
inscur.execute(inssql)
dbconn.commit()

mycursor.execute("SELECT * FROM t_user")
#leggo tutti i record in una sola volta
myresult = mycursor.fetchall()
print(myresult)