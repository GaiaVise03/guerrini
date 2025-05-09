from utente import Utente
from gestUser import GestUser


n=input("dimmi nome: ")
c=input("dimmi nome: ")
m=input("dimmi mail: ")
p=input("dimmi pwd:")
ut1= Utente(c,n,m,p)
ut1.salutaFormale()
mariobross= GestUser()
mariobross.createUser(c,n,m,p)