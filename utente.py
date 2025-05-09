class Utente:
    #attibuto non obbligatorio della classe
    tel=""
    id_user=-1
    #metodo per costruire oggetto della classe
    def __init__(self, cognome,nome,email,pwd="---"):
        #attibuti obbligatori della classe
        self.cognome=cognome
        self.nome=nome
        self.mail=email
        self.pwd=pwd
        

    def saluta(self):
        frase="Ciao sono " + self.nome + " " + self.cognome
        print(frase)

    def salutaFormale(self):
        frase="Buongiorno sono " + self.cognome + " " + self.nome
        print(frase)

