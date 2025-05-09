########### inizio codice standard   ###################################
########### inizio codice standard   ###################################
from PySide6.QtWidgets import QApplication, QMainWindow
import sys


#importo la classe generata da compilatore ui-> py
#dal file Ui_qtgui.py importo la classe Ui_MainWindow
#ora posso usare Ui_MainWindow

#!!!!!!!!!!!!!!cambiare nome classe from!!!!!!!
from prova import Ui_MainWindow


#creo mia classe MainWindow che eredita le caratteristiche della classe
# QMainWindow finestra base con solo bordi e x in alto per chiudere
class MainWindow(QMainWindow):
    #nel costruttore inserisco tutto il codice per gestire 
    #la finestra e gli oggetti da caricare dentro
   
    def __init__(self, parent=None):
        #lancio il costruttore di base di QmainWindow con super (la classe da cui derivo)
        super(MainWindow, self).__init__()
        #creo un attributo mio chiamato user interface ui
        # in cui metto un oggetto di tipo finestra compilata da qt
        self.ui=Ui_MainWindow()
        #lancio il metodo setupUI fornito dal compilatore
        self.ui.setupUi(self)
        # aggancio ai pulsanti il click che lancia i relativi metodi
        self.ui.btnWelcome.clicked.connect(self.showMsg)
        self.ui.btnPlus.clicked.connect(self.showPlusMsg)
        
    def showMsg(self):
        #refresh di display
        #creo nuovo testo pulito
        newtx=self.ui.elCognome.text() + " " +self.ui.elNome.text()
        self.ui.lblMsg.setText(newtx)

    def showPlusMsg(self):
        #refresh di display
        #creo nuovo testo pulito
        n1= int(self.ui.elNum1.text())
        n2= int(self.ui.elNum2.text())
        tot=n1+n2
        newtx=f"totale = {tot}"
        self.ui.lblMsg.setText(newtx)
 






######## inizio codice standard###################################
#creazione applicazione da poi eseguire in windows
app = QApplication(sys.argv)
#creazione di oggetto window grafico con tutti gli elementi grafici dati da setupUi
window = MainWindow()
# rende visibile la finestra
window.show()
# lancia la reale esecuzione della finestra windows
# e quindi del programma python
app.exec()
######## fine codice standard###################################
